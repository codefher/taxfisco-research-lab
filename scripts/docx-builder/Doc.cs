using DocumentFormat.OpenXml;
using DocumentFormat.OpenXml.Packaging;
using DocumentFormat.OpenXml.Wordprocessing;
using A = DocumentFormat.OpenXml.Drawing;
using DW = DocumentFormat.OpenXml.Drawing.Wordprocessing;
using PIC = DocumentFormat.OpenXml.Drawing.Pictures;

namespace Builder;

/// <summary>
/// Helpers OpenXML para construir un capitulo academico en formato APA 7.
/// Backend S (OpenXML SDK directo), con las recetas de tabla de tres lineas
/// horizontales que exige la norma y las convenciones tipograficas de la
/// guia de redaccion v7 (numeros con coma decimal, cursivas estadisticas).
/// </summary>
public sealed class Ctx
{
    public MainDocumentPart Main;
    public Body Body;
    public string ImageDir;
    public uint DocPropId = 1;

    // -- Runs ----------------------------------------------------------
    /// <summary>
    /// Convierte texto con marcas *cursiva* en runs con formato.
    /// El parametro italic fuerza el estado y anula el de la marca.
    /// </summary>
    public static List<Run> Runs(string text, bool bold = false, int? halfPt = null, string color = null, bool? italic = null)
    {
        var runs = new List<Run>();
        var parts = text.Split('*');
        for (int i = 0; i < parts.Length; i++)
        {
            if (parts[i].Length == 0) continue;
            var rPr = new RunProperties();
            if (bold) { rPr.Append(new Bold()); rPr.Append(new BoldComplexScript()); }
            bool cursiva = italic ?? (i % 2 == 1);
            if (cursiva) { rPr.Append(new Italic()); rPr.Append(new ItalicComplexScript()); }
            else if (italic == false) { rPr.Append(new Italic { Val = false }); rPr.Append(new ItalicComplexScript { Val = false }); }
            if (color != null) rPr.Append(new Color { Val = color });
            if (halfPt.HasValue)
            {
                rPr.Append(new FontSize { Val = halfPt.Value.ToString() });
                rPr.Append(new FontSizeComplexScript { Val = halfPt.Value.ToString() });
            }
            var run = new Run();
            if (rPr.HasChildren) run.Append(rPr);
            run.Append(new Text(parts[i]) { Space = SpaceProcessingModeValues.Preserve });
            runs.Add(run);
        }
        if (runs.Count == 0) runs.Add(new Run(new Text("") { Space = SpaceProcessingModeValues.Preserve }));
        return runs;
    }

    // -- Paragraphs ----------------------------------------------------
    public Paragraph P(string text, bool indent = true, JustificationValues? just = null)
    {
        var pPr = new ParagraphProperties();
        pPr.Append(new ParagraphStyleId { Val = "Normal" });
        pPr.Append(new SpacingBetweenLines { After = "0", Line = "480", LineRule = LineSpacingRuleValues.Auto });
        if (indent) pPr.Append(new Indentation { FirstLine = "720" });
        pPr.Append(new Justification { Val = just ?? JustificationValues.Both });
        var p = new Paragraph(pPr);
        foreach (var r in Runs(text)) p.Append(r);
        return p;
    }

    public Paragraph PLead(string text) => P(text, indent: false);

    public Paragraph Heading(string text, int level)
    {
        var pPr = new ParagraphProperties();
        pPr.Append(new ParagraphStyleId { Val = "Heading" + level });
        pPr.Append(new KeepNext());
        pPr.Append(new SpacingBetweenLines { Before = (level == 1 ? "360" : "280"), After = "120", Line = "240", LineRule = LineSpacingRuleValues.Auto });
        pPr.Append(new Justification { Val = JustificationValues.Left });
        pPr.Append(new OutlineLevel { Val = level - 1 });
        var p = new Paragraph(pPr);
        foreach (var r in Runs(text, bold: level <= 2)) p.Append(r);
        return p;
    }

    public void PageBreak() => Body.Append(new Paragraph(new Run(new Break { Type = BreakValues.Page })));

    // -- APA table -----------------------------------------------------
    /// <summary>Numero y titulo en cursiva, alineados a la izquierda.</summary>
    public void TableTitle(int number, string title)
    {
        var p1 = new Paragraph(new ParagraphProperties(
            new ParagraphStyleId { Val = "TableTitle" },
            new KeepNext(),
            new SpacingBetweenLines { Before = "240", After = "0", Line = "240", LineRule = LineSpacingRuleValues.Auto }));
        foreach (var r in Runs("Tabla " + number, bold: true, halfPt: 22, italic: false)) p1.Append(r);
        Body.Append(p1);

        var p2 = new Paragraph(new ParagraphProperties(
            new ParagraphStyleId { Val = "TableTitle" },
            new KeepNext(),
            new SpacingBetweenLines { Before = "0", After = "80", Line = "240", LineRule = LineSpacingRuleValues.Auto }));
        foreach (var r in Runs(title, halfPt: 22)) p2.Append(r);
        Body.Append(p2);
    }

    /// <summary>Nota al pie de tabla con la palabra Nota. en cursiva.</summary>
    public void TableNote(string text)
    {
        var p = new Paragraph(new ParagraphProperties(
            new ParagraphStyleId { Val = "TableNote" },
            new SpacingBetweenLines { Before = "60", After = "240", Line = "240", LineRule = LineSpacingRuleValues.Auto }));
        foreach (var r in Runs("Nota. ", halfPt: 20)) p.Append(r);
        foreach (var r in Runs(text, halfPt: 20)) p.Append(r);
        Body.Append(p);
    }

    /// <summary>
    /// Tabla APA 7 con tres lineas horizontales, sin lineas verticales.
    /// widths: anchos de columna en dxa, deben sumar 9360.
    /// </summary>
    public void Table(string[] headers, string[][] rows, int[] widths, bool[] rightAlign = null)
    {
        var tbl = new Table();
        var tblPr = new TableProperties();
        tblPr.Append(new TableWidth { Width = "5000", Type = TableWidthUnitValues.Pct });
        tblPr.Append(new TableBorders(
            new TopBorder { Val = BorderValues.Single, Size = 8, Space = 0, Color = "000000" },
            new BottomBorder { Val = BorderValues.Single, Size = 8, Space = 0, Color = "000000" },
            new LeftBorder { Val = BorderValues.None },
            new RightBorder { Val = BorderValues.None },
            new InsideHorizontalBorder { Val = BorderValues.None },
            new InsideVerticalBorder { Val = BorderValues.None }));
        tblPr.Append(new TableLayout { Type = TableLayoutValues.Fixed });
        tblPr.Append(new TableCellMarginDefault(
            new TopMargin { Width = "40", Type = TableWidthUnitValues.Dxa },
            new TableCellLeftMargin { Width = 80, Type = TableWidthValues.Dxa },
            new BottomMargin { Width = "40", Type = TableWidthUnitValues.Dxa },
            new TableCellRightMargin { Width = 80, Type = TableWidthValues.Dxa }));
        tblPr.Append(new TableLook { Val = "04A0" });
        tbl.Append(tblPr);

        var grid = new TableGrid();
        foreach (var w in widths) grid.Append(new GridColumn { Width = w.ToString() });
        tbl.Append(grid);

        // Encabezado
        var hr = new TableRow(new TableRowProperties(
            new TableHeader(),
            new CantSplit()));
        for (int i = 0; i < headers.Length; i++)
        {
            hr.Append(Cell(headers[i], widths[i], true, false,
                rightAlign != null && rightAlign[i], true));
        }
        tbl.Append(hr);

        foreach (var row in rows)
        {
            var tr = new TableRow(new TableRowProperties(new CantSplit()));
            for (int i = 0; i < headers.Length; i++)
            {
                tr.Append(Cell(row[i], widths[i], false, false,
                    rightAlign != null && rightAlign[i], false));
            }
            tbl.Append(tr);
        }
        Body.Append(tbl);
    }

    private TableCell Cell(string text, int width, bool bold, bool italic, bool right, bool header)
    {
        var tcPr = new TableCellProperties();
        tcPr.Append(new TableCellWidth { Width = width.ToString(), Type = TableWidthUnitValues.Dxa });
        if (header)
        {
            tcPr.Append(new TableCellBorders(
                new BottomBorder { Val = BorderValues.Single, Size = 6, Space = 0, Color = "000000" }));
        }
        tcPr.Append(new TableCellVerticalAlignment { Val = TableVerticalAlignmentValues.Top });
        var tc = new TableCell(tcPr);
        var p = new Paragraph(new ParagraphProperties(
            new ParagraphStyleId { Val = "TableText" },
            new SpacingBetweenLines { Before = "40", After = "40", Line = "240", LineRule = LineSpacingRuleValues.Auto },
            new Justification { Val = right ? JustificationValues.Right : JustificationValues.Left }));
        foreach (var r in Runs(text, bold, 20, null)) p.Append(r);
        tc.Append(p);
        return tc;
    }

    // -- Figures -------------------------------------------------------
    /// <summary>Numero de figura en negrita y titulo en cursiva, sobre la imagen.</summary>
    public void FigureTitle(int number, string title)
    {
        var p1 = new Paragraph(new ParagraphProperties(
            new ParagraphStyleId { Val = "FigureCaption" },
            new KeepNext(),
            new SpacingBetweenLines { Before = "240", After = "0", Line = "240", LineRule = LineSpacingRuleValues.Auto }));
        foreach (var r in Runs("Figura " + number, bold: true, halfPt: 22, italic: false)) p1.Append(r);
        Body.Append(p1);

        var p2 = new Paragraph(new ParagraphProperties(
            new ParagraphStyleId { Val = "FigureCaption" },
            new KeepNext(),
            new SpacingBetweenLines { Before = "0", After = "120", Line = "240", LineRule = LineSpacingRuleValues.Auto }));
        foreach (var r in Runs(title, halfPt: 22)) p2.Append(r);
        Body.Append(p2);
    }

    /// <summary>Nota al pie de figura con la palabra Nota. en cursiva.</summary>
    public void FigureNote(string text)
    {
        var nt = new Paragraph(new ParagraphProperties(
            new ParagraphStyleId { Val = "TableNote" },
            new SpacingBetweenLines { Before = "40", After = "240", Line = "240", LineRule = LineSpacingRuleValues.Auto }));
        foreach (var r in Runs("Nota. ", halfPt: 20)) nt.Append(r);
        foreach (var r in Runs(text, halfPt: 20)) nt.Append(r);
        Body.Append(nt);
    }

    /// <summary>
    /// Inserta la imagen de la figura. El alto se calcula a partir de las
    /// dimensiones reales del PNG, que se leen de la cabecera IHDR.
    /// </summary>
    public void FigureImage(string fileName, int number, string altText, int widthPx)
    {
        var path = Path.Combine(ImageDir, fileName);
        if (!File.Exists(path))
        {
            var enGraficos = Path.Combine(ImageDir, "graficos", fileName);
            if (File.Exists(enGraficos)) path = enGraficos;
            else
            {
                var enTarjetas = Path.Combine(ImageDir, "tarjetas-kpi", fileName);
                if (File.Exists(enTarjetas)) path = enTarjetas;
            }
        }
        if (!File.Exists(path)) { Body.Append(new Paragraph(new Run(new Text("[figura no encontrada: " + fileName + "]")))); return; }

        var imgPart = Main.AddImagePart(ImagePartType.Png);
        using (var fs = File.OpenRead(path)) imgPart.FeedData(fs);
        string relId = Main.GetIdOfPart(imgPart);

        var (w, h) = PngSize(path);
        int heightPx = (int)Math.Round(widthPx * (h / (double)w));

        // Limita el alto para que el bloque titulo + imagen + nota quepa en una pagina.
        const int ALTO_MAX_PX = 480; // 5.0 pulgadas a 96 dpi
        if (heightPx > ALTO_MAX_PX)
        {
            widthPx = (int)Math.Round(widthPx * (ALTO_MAX_PX / (double)heightPx));
            heightPx = ALTO_MAX_PX;
        }

        long cx = widthPx * 9525L;
        long cy = heightPx * 9525L;
        uint id = DocPropId++;

        var pic = new PIC.Picture(
            new PIC.NonVisualPictureProperties(
                new PIC.NonVisualDrawingProperties { Id = 0U, Name = fileName },
                new PIC.NonVisualPictureDrawingProperties()),
            new PIC.BlipFill(
                new A.Blip { Embed = relId },
                new A.Stretch(new A.FillRectangle())),
            new PIC.ShapeProperties(
                new A.Transform2D(new A.Offset { X = 0L, Y = 0L }, new A.Extents { Cx = cx, Cy = cy }),
                new A.PresetGeometry(new A.AdjustValueList()) { Preset = A.ShapeTypeValues.Rectangle }));

        var drawing = new Drawing(new DW.Inline(
            new DW.Extent { Cx = cx, Cy = cy },
            new DW.EffectExtent { LeftEdge = 0L, TopEdge = 0L, RightEdge = 0L, BottomEdge = 0L },
            new DW.DocProperties { Id = id, Name = "Figura " + number, Description = altText },
            new DW.NonVisualGraphicFrameDrawingProperties(new A.GraphicFrameLocks { NoChangeAspect = true }),
            new A.Graphic(new A.GraphicData(pic) { Uri = "http://schemas.openxmlformats.org/drawingml/2006/picture" }))
        {
            DistanceFromTop = 0U, DistanceFromBottom = 0U, DistanceFromLeft = 0U, DistanceFromRight = 0U
        });

        var p = new Paragraph(new ParagraphProperties(
            new ParagraphStyleId { Val = "FigureImage" },
            new SpacingBetweenLines { Before = "120", After = "60", Line = "240", LineRule = LineSpacingRuleValues.Auto },
            new Justification { Val = JustificationValues.Center }));
        p.Append(new Run(drawing));
        Body.Append(p);
    }

    /// <summary>Lee el ancho y el alto reales de un PNG desde su cabecera IHDR.</summary>
    public static (int w, int h) PngSize(string path)
    {
        var bytes = File.ReadAllBytes(path);
        if (bytes.Length < 24) throw new InvalidDataException("El archivo no es un PNG valido: " + path);
        int w = (bytes[16] << 24) | (bytes[17] << 16) | (bytes[18] << 8) | bytes[19];
        int h = (bytes[20] << 24) | (bytes[21] << 16) | (bytes[22] << 8) | bytes[23];
        return (w, h);
    }

    // -- Cover and references ------------------------------------------
    /// <summary>Linea de portada, centrada.</summary>
    public void Cover(string text, bool title = false, bool bold = false)
    {
        var pPr = new ParagraphProperties(
            new ParagraphStyleId { Val = title ? "CoverTitle" : "CoverText" },
            new SpacingBetweenLines
            {
                Before = "0",
                After = title ? "240" : "120",
                Line = "276",
                LineRule = LineSpacingRuleValues.Auto
            },
            new Justification { Val = JustificationValues.Center });
        var p = new Paragraph(pPr);
        foreach (var r in Runs(text, bold: bold, halfPt: title ? 32 : 26)) p.Append(r);
        Body.Append(p);
    }

    /// <summary>Entrada de la lista de referencias con sangria francesa.</summary>
    public void Ref(string text)
    {
        var pPr = new ParagraphProperties(
            new ParagraphStyleId { Val = "Normal" },
            new Indentation { Left = "720", Hanging = "720" },
            new SpacingBetweenLines { After = "0", Line = "480", LineRule = LineSpacingRuleValues.Auto },
            new Justification { Val = JustificationValues.Left });
        var p = new Paragraph(pPr);
        foreach (var r in Runs(text)) p.Append(r);
        Body.Append(p);
    }

    // -- TOC field -----------------------------------------------------
    /// <summary>
    /// Tabla de contenido como campo de Word. El resultado queda escrito con
    /// las entradas y sus paginas, de manera que el documento ya se ve completo
    /// sin actualizar el campo, y Word lo recalcula con Ctrl+E y F9.
    /// </summary>
    public void Toc(List<(string titulo, int pagina)> entradas)
    {
        for (int i = 0; i < entradas.Count; i++)
        {
            var (titulo, pagina) = entradas[i];
            var pPr = new ParagraphProperties(
                new ParagraphStyleId { Val = "Normal" },
                new Tabs(new TabStop
                {
                    Val = TabStopValues.Right,
                    Position = 9360,
                    Leader = TabStopLeaderCharValues.Dot
                }),
                new SpacingBetweenLines { After = "60", Line = "240", LineRule = LineSpacingRuleValues.Auto },
                new Justification { Val = JustificationValues.Left });
            var p = new Paragraph(pPr);
            if (i == 0)
            {
                p.Append(new Run(new FieldChar { FieldCharType = FieldCharValues.Begin }));
                p.Append(new Run(new FieldCode(" TOC \\o \"1-3\" \\h \\z \\u ") { Space = SpaceProcessingModeValues.Preserve }));
                p.Append(new Run(new FieldChar { FieldCharType = FieldCharValues.Separate }));
            }
            foreach (var r in Runs(titulo, halfPt: 24)) p.Append(r);
            p.Append(new Run(new TabChar()));
            p.Append(new Run(new RunProperties(new FontSize { Val = "24" }),
                new Text(pagina.ToString()) { Space = SpaceProcessingModeValues.Preserve }));
            if (i == entradas.Count - 1)
            {
                p.Append(new Run(new FieldChar { FieldCharType = FieldCharValues.End }));
            }
            Body.Append(p);
        }
    }
}
