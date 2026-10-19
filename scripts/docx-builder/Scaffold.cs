using DocumentFormat.OpenXml;
using DocumentFormat.OpenXml.Packaging;
using DocumentFormat.OpenXml.Wordprocessing;

namespace Builder;

/// <summary>
/// Armazon del documento: estilos, encabezado con numero de pagina, seccion.
/// El orden de los elementos importa en OpenXML, de modo que las propiedades
/// de seccion se agregan al final, una vez construido el cuerpo.
/// </summary>
public static class Scaffold
{
    private const string FONT = "Times New Roman";

    public static (WordprocessingDocument, MainDocumentPart, Body) Create(string outputPath, string runningHead)
    {
        if (File.Exists(outputPath)) File.Delete(outputPath);
        var doc = WordprocessingDocument.Create(outputPath, WordprocessingDocumentType.Document);
        var main = doc.AddMainDocumentPart();
        main.Document = new Document();
        var body = new Body();
        main.Document.Append(body);

        AddStyles(main);
        AddHeader(main, runningHead);

        return (doc, main, body);
    }

    /// <summary>Agrega las propiedades de seccion, que deben cerrar el cuerpo.</summary>
    public static void Close(MainDocumentPart main, Body body)
    {
        var firstHeader = main.AddNewPart<HeaderPart>();
        firstHeader.Header = new Header(new Paragraph(
            new ParagraphProperties(new ParagraphStyleId { Val = "HeaderFooter" })));

        body.Append(new SectionProperties(
            new HeaderReference { Type = HeaderFooterValues.First, Id = main.GetIdOfPart(firstHeader) },
            new HeaderReference { Type = HeaderFooterValues.Default, Id = main.GetIdOfPart(main.HeaderParts.First()) },
            new TitlePage(),
            new PageSize { Width = 12240, Height = 15840 },
            new PageMargin { Top = 1440, Right = 1440, Bottom = 1440, Left = 1440, Header = 720, Footer = 720, Gutter = 0 },
            new Columns { Space = "708" },
            new DocGrid { LinePitch = 360 }));
    }

    private static void AddHeader(MainDocumentPart main, string runningHead)
    {
        var hp = main.AddNewPart<HeaderPart>();
        var p = new Paragraph(new ParagraphProperties(
            new ParagraphStyleId { Val = "HeaderFooter" },
            new Tabs(new TabStop { Val = TabStopValues.Right, Position = 9360 }),
            new SpacingBetweenLines { After = "0", Line = "240", LineRule = LineSpacingRuleValues.Auto }));
        p.Append(new Run(new RunProperties(new FontSize { Val = "20" }), new Text(runningHead) { Space = SpaceProcessingModeValues.Preserve }));
        p.Append(new Run(new TabChar()));
        p.Append(new Run(new FieldChar { FieldCharType = FieldCharValues.Begin }));
        p.Append(new Run(new FieldCode(" PAGE ") { Space = SpaceProcessingModeValues.Preserve }));
        p.Append(new Run(new FieldChar { FieldCharType = FieldCharValues.Separate }));
        p.Append(new Run(new RunProperties(new FontSize { Val = "20" }), new Text("1")));
        p.Append(new Run(new FieldChar { FieldCharType = FieldCharValues.End }));
        hp.Header = new Header(p);
    }

    private static void AddStyles(MainDocumentPart main)
    {
        var part = main.AddNewPart<StyleDefinitionsPart>();
        var styles = new Styles();

        // -- defaults --
        styles.Append(new DocDefaults(
            new RunPropertiesDefault(new RunPropertiesBaseStyle(
                new RunFonts { Ascii = FONT, HighAnsi = FONT, ComplexScript = FONT, EastAsia = FONT },
                new FontSize { Val = "24" },
                new FontSizeComplexScript { Val = "24" },
                new Languages { Val = "es-BO" })),
            new ParagraphPropertiesDefault(new ParagraphPropertiesBaseStyle(
                new SpacingBetweenLines { After = "0", Line = "480", LineRule = LineSpacingRuleValues.Auto }))));

        // -- Normal --
        styles.Append(new Style(
            new StyleName { Val = "Normal" },
            new PrimaryStyle())
        {
            Type = StyleValues.Paragraph, StyleId = "Normal", Default = true,
            StyleParagraphProperties = new StyleParagraphProperties(
                new SpacingBetweenLines { After = "0", Line = "480", LineRule = LineSpacingRuleValues.Auto },
                new Justification { Val = JustificationValues.Both })
        });

        // -- Headings --
        for (int lv = 1; lv <= 3; lv++)
        {
            int size = lv == 1 ? 28 : (lv == 2 ? 26 : 24);
            var sp = new StyleParagraphProperties(
                new KeepNext(), new KeepLines(),
                new SpacingBetweenLines { Before = lv == 1 ? "360" : "280", After = "120", Line = "240", LineRule = LineSpacingRuleValues.Auto },
                new Justification { Val = JustificationValues.Left },
                new OutlineLevel { Val = lv - 1 });
            styles.Append(new Style(
                new StyleName { Val = "heading " + lv },
                new BasedOn { Val = "Normal" },
                new NextParagraphStyle { Val = "Normal" },
                new UIPriority { Val = 9 },
                new PrimaryStyle())
            {
                Type = StyleValues.Paragraph, StyleId = "Heading" + lv,
                StyleParagraphProperties = sp,
                StyleRunProperties = new StyleRunProperties(
                    new RunFonts { Ascii = FONT, HighAnsi = FONT, ComplexScript = FONT },
                    new Bold(), new BoldComplexScript(),
                    new Color { Val = "000000" },
                    new FontSize { Val = size.ToString() },
                    new FontSizeComplexScript { Val = size.ToString() })
            });
        }

        // -- Table title (cursiva) --
        styles.Append(new Style(
            new StyleName { Val = "Table Title" },
            new BasedOn { Val = "Normal" },
            new NextParagraphStyle { Val = "Normal" })
        {
            Type = StyleValues.Paragraph, StyleId = "TableTitle",
            StyleParagraphProperties = new StyleParagraphProperties(
                new SpacingBetweenLines { Before = "240", After = "80", Line = "240", LineRule = LineSpacingRuleValues.Auto },
                new Justification { Val = JustificationValues.Left }),
            StyleRunProperties = new StyleRunProperties(
                new RunFonts { Ascii = FONT, HighAnsi = FONT, ComplexScript = FONT },
                new Italic(), new ItalicComplexScript(),
                new FontSize { Val = "22" }, new FontSizeComplexScript { Val = "22" })
        });

        // -- Table text --
        styles.Append(new Style(
            new StyleName { Val = "Table Text" },
            new BasedOn { Val = "Normal" })
        {
            Type = StyleValues.Paragraph, StyleId = "TableText",
            StyleParagraphProperties = new StyleParagraphProperties(
                new SpacingBetweenLines { Before = "40", After = "40", Line = "240", LineRule = LineSpacingRuleValues.Auto },
                new Justification { Val = JustificationValues.Left }),
            StyleRunProperties = new StyleRunProperties(
                new RunFonts { Ascii = FONT, HighAnsi = FONT, ComplexScript = FONT },
                new FontSize { Val = "20" }, new FontSizeComplexScript { Val = "20" })
        });

        // -- Table note --
        styles.Append(new Style(
            new StyleName { Val = "Table Note" },
            new BasedOn { Val = "Normal" })
        {
            Type = StyleValues.Paragraph, StyleId = "TableNote",
            StyleParagraphProperties = new StyleParagraphProperties(
                new SpacingBetweenLines { Before = "60", After = "240", Line = "240", LineRule = LineSpacingRuleValues.Auto },
                new Justification { Val = JustificationValues.Left }),
            StyleRunProperties = new StyleRunProperties(
                new RunFonts { Ascii = FONT, HighAnsi = FONT, ComplexScript = FONT },
                new FontSize { Val = "20" }, new FontSizeComplexScript { Val = "20" })
        });

        // -- Figure caption --
        styles.Append(new Style(
            new StyleName { Val = "Figure Caption" },
            new BasedOn { Val = "Normal" })
        {
            Type = StyleValues.Paragraph, StyleId = "FigureCaption",
            StyleParagraphProperties = new StyleParagraphProperties(
                new SpacingBetweenLines { Before = "0", After = "0", Line = "240", LineRule = LineSpacingRuleValues.Auto },
                new Justification { Val = JustificationValues.Left }),
            StyleRunProperties = new StyleRunProperties(
                new RunFonts { Ascii = FONT, HighAnsi = FONT, ComplexScript = FONT },
                new FontSize { Val = "22" }, new FontSizeComplexScript { Val = "22" })
        });

        // -- Figure image --
        styles.Append(new Style(
            new StyleName { Val = "Figure Image" },
            new BasedOn { Val = "Normal" })
        {
            Type = StyleValues.Paragraph, StyleId = "FigureImage",
            StyleParagraphProperties = new StyleParagraphProperties(
                new SpacingBetweenLines { Before = "160", After = "60", Line = "240", LineRule = LineSpacingRuleValues.Auto },
                new Justification { Val = JustificationValues.Center })
        });

        // -- Header/footer --
        styles.Append(new Style(
            new StyleName { Val = "Header Footer" },
            new BasedOn { Val = "Normal" })
        {
            Type = StyleValues.Paragraph, StyleId = "HeaderFooter",
            StyleParagraphProperties = new StyleParagraphProperties(
                new SpacingBetweenLines { After = "0", Line = "240", LineRule = LineSpacingRuleValues.Auto }),
            StyleRunProperties = new StyleRunProperties(
                new RunFonts { Ascii = FONT, HighAnsi = FONT, ComplexScript = FONT },
                new FontSize { Val = "20" }, new FontSizeComplexScript { Val = "20" })
        });

        // -- Cover styles --
        styles.Append(new Style(
            new StyleName { Val = "Cover Title" },
            new BasedOn { Val = "Normal" })
        {
            Type = StyleValues.Paragraph, StyleId = "CoverTitle",
            StyleParagraphProperties = new StyleParagraphProperties(
                new SpacingBetweenLines { Before = "0", After = "240", Line = "276", LineRule = LineSpacingRuleValues.Auto },
                new Justification { Val = JustificationValues.Center }),
            StyleRunProperties = new StyleRunProperties(
                new RunFonts { Ascii = FONT, HighAnsi = FONT, ComplexScript = FONT },
                new Bold(), new BoldComplexScript(),
                new FontSize { Val = "32" }, new FontSizeComplexScript { Val = "32" })
        });

        styles.Append(new Style(
            new StyleName { Val = "Cover Text" },
            new BasedOn { Val = "Normal" })
        {
            Type = StyleValues.Paragraph, StyleId = "CoverText",
            StyleParagraphProperties = new StyleParagraphProperties(
                new SpacingBetweenLines { Before = "0", After = "120", Line = "276", LineRule = LineSpacingRuleValues.Auto },
                new Justification { Val = JustificationValues.Center }),
            StyleRunProperties = new StyleRunProperties(
                new RunFonts { Ascii = FONT, HighAnsi = FONT, ComplexScript = FONT },
                new FontSize { Val = "26" }, new FontSizeComplexScript { Val = "26" })
        });

        part.Styles = styles;
    }
}
