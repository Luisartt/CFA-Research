from __future__ import annotations

import copy
from collections.abc import Callable
from pathlib import Path
from typing import Any

import pytest
from deck_fixtures import (  # noqa: F401  (import first: sets sys.path)
    OUTLINE,
    deck_project,
    logo_template,
    no_subtitle_template,
    potx_from,
    section_mid_title_template,
    spanish_template,
    thin_bar_template,
    title_and_blank_template,
    vertical_title_template,
    write_deck_project,
)
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE, PP_PLACEHOLDER
from pptx.util import Emu

from build_pptx import SOURCES_NAME, main, pick_layout


def _build(project: Path) -> Any:
    assert main(["--project", str(project)]) == 0
    return Presentation(str(project / "pitch" / "ACME_deck_v1.pptx"))


def test_one_slide_per_outline_entry_and_template_examples_removed(deck_project: Path) -> None:
    prs = _build(deck_project)
    assert len(prs.slides) == len(OUTLINE["slides"])
    titles = [s.shapes.title.text if s.shapes.title is not None else "" for s in prs.slides]
    assert "Example slide from the template" not in titles
    assert titles[1] == "Investment thesis"


def test_sources_footer_on_every_slide_but_the_title(deck_project: Path) -> None:
    prs = _build(deck_project)
    for i, slide in enumerate(prs.slides):
        if i == 0:
            continue
        footers = [sh for sh in slide.shapes if sh.name == SOURCES_NAME]
        assert len(footers) == 1, i
        assert footers[0].text_frame.text.startswith("Source: ")


def test_speaker_notes_in_the_notes_field(deck_project: Path) -> None:
    prs = _build(deck_project)
    notes = prs.slides[1].notes_slide.notes_text_frame.text
    assert "Ana" in notes and "Three pillars." in notes


def test_charts_placed_inside_the_slide(deck_project: Path) -> None:
    prs = _build(deck_project)
    pictures = [sh for s in prs.slides for sh in s.shapes if sh.shape_type == MSO_SHAPE_TYPE.PICTURE]
    assert len(pictures) == 2
    for slide in prs.slides:
        for sh in slide.shapes:
            if sh.left is None or sh.width is None:
                continue
            assert sh.left >= 0 and sh.top >= 0
            assert sh.left + sh.width <= prs.slide_width and sh.top + sh.height <= prs.slide_height


def test_bullets_land_on_the_slide(deck_project: Path) -> None:
    prs = _build(deck_project)
    text = " ".join(sh.text_frame.text for sh in prs.slides[1].shapes if sh.has_text_frame)
    assert "Volume recovery" in text and "Margin expansion" in text


def test_no_empty_placeholders_left(deck_project: Path) -> None:
    prs = _build(deck_project)
    for slide in prs.slides:
        for ph in slide.placeholders:
            assert not ph.has_text_frame or ph.text_frame.text.strip(), ph.name


def test_versions_are_never_overwritten(deck_project: Path) -> None:
    _build(deck_project)
    assert main(["--project", str(deck_project)]) == 0
    assert (deck_project / "pitch" / "ACME_deck_v2.pptx").is_file()


def test_plain_default_when_no_template(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    project = write_deck_project(tmp_path, template=False)
    assert main(["--project", str(project)]) == 0
    out = capsys.readouterr().out
    assert out.isascii() and "no template" in out


def test_missing_sources_is_an_error(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    outline = copy.deepcopy(OUTLINE)
    outline["slides"][1]["sources"] = ""
    project = write_deck_project(tmp_path, outline=outline)
    assert main(["--project", str(project)]) == 2
    assert "sources" in capsys.readouterr().out


def test_missing_chart_is_an_error(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    project = write_deck_project(tmp_path, charts=False)
    assert main(["--project", str(project)]) == 2
    assert "revenue-margin" in capsys.readouterr().out


def test_long_outline_warns_about_time(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    outline = copy.deepcopy(OUTLINE)
    outline["slides"][1]["minutes"] = 9
    project = write_deck_project(tmp_path, outline=outline)
    assert main(["--project", str(project)]) == 0
    assert "minutes" in capsys.readouterr().out


def test_list_layouts(deck_project: Path, capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["--project", str(deck_project), "--list-layouts"]) == 0
    out = capsys.readouterr().out
    assert out.isascii() and "Title Slide" in out and "Two Content" in out


def test_layout_choice_on_the_default_template() -> None:
    prs = Presentation()
    assert pick_layout(prs, "title", False).name == "Title Slide"
    assert pick_layout(prs, "section", False).name == "Section Header"
    assert pick_layout(prs, "content", False).name == "Title and Content"
    assert pick_layout(prs, "content", True).name == "Two Content"
    assert pick_layout(prs, "chart", True).name == "Title Only"


# --- layout choice by geometry (synthetic templates reproduce real-template failures) ----------

EMU_IN = 914400


def _bottom(shape: Any) -> int:
    return int(shape.top + shape.height)


def _overlaps(a: Any, b: Any) -> bool:
    return bool(a.left < b.left + b.width and b.left < a.left + a.width
                and a.top < b.top + b.height and b.top < a.top + a.height)


def _pictures(slide: Any) -> list[Any]:
    return [sh for sh in slide.shapes if sh.shape_type == MSO_SHAPE_TYPE.PICTURE]


def _with_text(slide: Any, text: str) -> Any:
    return next(sh for sh in slide.shapes if sh.has_text_frame and text in sh.text_frame.text)


def _build_on(project: Path, make: Callable[[Path], Path]) -> Any:
    make(project / "pitch" / "template.pptx")
    return _build(project)


def test_thin_heading_bar_body_is_not_used_for_bullets(deck_project: Path) -> None:
    template = thin_bar_template(deck_project / "pitch" / "template.pptx")
    assert pick_layout(Presentation(str(template)), "content", False).name == "1-Up"
    prs = _build(deck_project)
    body = _with_text(prs.slides[1], "Volume recovery")
    assert "Margin expansion" in body.text_frame.text
    assert body.height >= 1.5 * EMU_IN
    assert not [sh for sh in prs.slides[1].placeholders if sh.height < 0.5 * EMU_IN]  # thin bar removed


def test_section_layout_with_mid_slide_title_is_not_used_for_charts(deck_project: Path) -> None:
    template = section_mid_title_template(deck_project / "pitch" / "template.pptx")
    prs = Presentation(str(template))
    assert pick_layout(prs, "chart", True).name == "Title Only"
    assert pick_layout(prs, "section", False).name == "Section Header"
    built = _build(deck_project)
    chart_slide = built.slides[3]
    assert chart_slide.slide_layout.name == "Title Only"
    assert _pictures(chart_slide)[0].top >= _bottom(chart_slide.shapes.title)


def test_vertical_title_layout_is_rejected_when_a_normal_one_exists(deck_project: Path) -> None:
    template = vertical_title_template(deck_project / "pitch" / "template.pptx")
    prs = Presentation(str(template))
    assert pick_layout(prs, "content", False).name == "Title and Content"
    built = _build(deck_project)
    for slide in list(built.slides)[1:4]:
        assert slide.shapes.title.top < 0.25 * built.slide_height
        assert slide.shapes.title.height <= 0.30 * built.slide_height


def test_all_vertical_titles_use_the_template_body_and_keep_charts_clear(deck_project: Path) -> None:
    prs = _build_on(deck_project, lambda p: vertical_title_template(p, only_vertical=True))
    for slide in list(prs.slides)[1:4]:
        for picture in _pictures(slide):
            assert not _overlaps(picture, slide.shapes.title)
    body = _with_text(prs.slides[1], "Volume recovery")
    assert body.is_placeholder and body.height >= 1.5 * EMU_IN


def test_spanish_layout_names_without_layout_types(tmp_path: Path) -> None:
    prs = Presentation(str(spanish_template(tmp_path / "es.pptx")))
    assert pick_layout(prs, "title", False).name == "Diapositiva de título"
    assert pick_layout(prs, "section", False).name == "Encabezado de sección"
    assert pick_layout(prs, "content", False).name == "Título y objetos"
    assert pick_layout(prs, "content", True).name == "Dos objetos"
    assert pick_layout(prs, "chart", True).name == "Solo el título"


def test_title_slide_without_subtitle_uses_its_body_and_warns(deck_project: Path,
                                                             capsys: pytest.CaptureFixture[str]) -> None:
    prs = _build_on(deck_project, no_subtitle_template)
    assert prs.slides[0].slide_layout.name == "Title Slide"
    subtitle = _with_text(prs.slides[0], "BUY - target")
    assert subtitle.is_placeholder
    out = capsys.readouterr().out
    assert out.isascii() and "[warn]" in out and "subtitle" in out


def test_no_subtitle_and_no_body_puts_subtitle_under_the_title(deck_project: Path,
                                                               capsys: pytest.CaptureFixture[str]) -> None:
    prs = _build_on(deck_project, lambda p: no_subtitle_template(p, with_body=False))
    slide = prs.slides[0]
    subtitle = _with_text(slide, "BUY - target")
    assert subtitle.top >= _bottom(slide.shapes.title)
    assert "subtitle" in capsys.readouterr().out


def test_content_area_is_below_the_title_and_above_the_footer_band(deck_project: Path) -> None:
    prs = _build(deck_project)
    master_footer = next(ph for ph in prs.slide_master.placeholders
                         if ph.placeholder_format.type == PP_PLACEHOLDER.FOOTER)
    for slide in prs.slides:
        for picture in _pictures(slide):
            assert picture.top >= _bottom(slide.shapes.title)
            assert _bottom(picture) <= master_footer.top


def test_content_area_starts_no_higher_than_the_master_body(deck_project: Path) -> None:
    """Templates draw bands between title and body; the master body top is where content starts."""
    template = deck_project / "pitch" / "template.pptx"
    prs = Presentation()
    body = next(ph for ph in prs.slide_master.placeholders if ph.placeholder_format.type == PP_PLACEHOLDER.BODY)
    body.top, body.height = Emu(int(2.4 * EMU_IN)), Emu(int(4.3 * EMU_IN))
    prs.save(str(template))
    built = _build(deck_project)
    assert _pictures(built.slides[3])[0].top >= int(2.4 * EMU_IN)


def test_title_mid_slide_only_template_moves_title_up_and_never_goes_negative(deck_project: Path) -> None:
    prs = _build_on(deck_project, title_and_blank_template)
    for slide in list(prs.slides)[1:4]:
        assert slide.shapes.title.top < 0.25 * prs.slide_height
        for shape in slide.shapes:
            assert shape.width > 0 and shape.height > 0
            assert shape.top >= 0 and _bottom(shape) <= prs.slide_height
        for picture in _pictures(slide):
            assert picture.top >= _bottom(slide.shapes.title)


PPR_ORDER = ["lnSpc", "spcBef", "spcAft", "buClrTx", "buClr", "buSzTx", "buSzPct", "buSzPts", "buFontTx", "buFont",
             "buNone", "buAutoNum", "buChar", "buBlip", "tabLst", "defRPr", "extLst"]


def test_fallback_bullets_are_real_bullets_in_schema_order(deck_project: Path) -> None:
    prs = _build_on(deck_project, title_and_blank_template)
    box = _with_text(prs.slides[1], "Volume recovery")
    assert not box.is_placeholder
    for paragraph in box.text_frame.paragraphs:
        tags = [child.tag.split("}")[1] for child in paragraph._p.pPr]
        assert "buChar" in tags
        assert tags == sorted(tags, key=PPR_ORDER.index)
        assert paragraph.runs and all(run.font.size is not None for run in paragraph.runs)


def test_sources_footer_sits_in_the_master_footer_band_clear_of_logos(deck_project: Path) -> None:
    logo = deck_project / "report" / "charts" / "revenue-margin.png"
    prs = _build_on(deck_project, lambda p: logo_template(p, logo))
    master_footer = next(ph for ph in prs.slide_master.placeholders
                         if ph.placeholder_format.type == PP_PLACEHOLDER.FOOTER)
    logo_shape = next(sh for sh in prs.slide_master.shapes if sh.shape_type == MSO_SHAPE_TYPE.PICTURE)
    for slide in list(prs.slides)[1:]:
        footer = next(sh for sh in slide.shapes if sh.name == SOURCES_NAME)
        assert footer.top == master_footer.top
        assert not _overlaps(footer, logo_shape)


@pytest.mark.parametrize(("language", "label"), [("en", "Source: "), ("es", "Fuente: "), ("pt", "Fonte: ")])
def test_sources_label_follows_the_deck_language(tmp_path: Path, language: str, label: str) -> None:
    outline = copy.deepcopy(OUTLINE)
    outline["deck"]["language"] = language
    prs = _build(write_deck_project(tmp_path, outline=outline))
    footers = [sh for s in list(prs.slides)[1:] for sh in s.shapes if sh.name == SOURCES_NAME]
    assert footers and all(f.text_frame.text.startswith(label) for f in footers)


# --- error paths -------------------------------------------------------------------------------

def test_potx_template_is_converted_in_memory(deck_project: Path) -> None:
    template = deck_project / "pitch" / "template.pptx"
    potx = potx_from(template, deck_project / "team.potx")
    template.unlink()
    assert main(["--project", str(deck_project), "--template", str(potx)]) == 0
    assert len(Presentation(str(deck_project / "pitch" / "ACME_deck_v1.pptx")).slides) == len(OUTLINE["slides"])
    assert main(["--project", str(deck_project), "--template", str(potx), "--list-layouts"]) == 0


def test_list_layouts_on_a_corrupt_template_exits_2(deck_project: Path, capsys: pytest.CaptureFixture[str]) -> None:
    (deck_project / "pitch" / "template.pptx").write_bytes(b"not a zip")
    assert main(["--project", str(deck_project), "--list-layouts"]) == 2
    out = capsys.readouterr().out
    assert out.isascii() and "not a valid" in out


def test_corrupt_chart_png_exits_2(deck_project: Path, capsys: pytest.CaptureFixture[str]) -> None:
    (deck_project / "report" / "charts" / "football-field.png").write_bytes(b"xx")
    assert main(["--project", str(deck_project)]) == 2
    out = capsys.readouterr().out
    assert "football-field" in out and "image" in out


def test_null_title_is_missing(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    outline = copy.deepcopy(OUTLINE)
    outline["slides"][1]["title"] = None
    assert main(["--project", str(write_deck_project(tmp_path, outline=outline))]) == 2
    assert "slide 2: title is missing" in capsys.readouterr().out


def test_chart_name_with_png_suffix_is_accepted(tmp_path: Path) -> None:
    outline = copy.deepcopy(OUTLINE)
    outline["slides"][3]["chart"] = "football-field.png"
    prs = _build(write_deck_project(tmp_path, outline=outline))
    assert len(_pictures(prs.slides[3])) == 1
