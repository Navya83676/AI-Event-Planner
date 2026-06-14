import os
import matplotlib.pyplot as plt
from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.platypus import Image
from reportlab.platypus import PageBreak
from reportlab.platypus import (
        SimpleDocTemplate,
        Paragraph,
        Spacer
    )

from reportlab.lib.styles import (
    getSampleStyleSheet
    )

from reportlab.lib.styles import ParagraphStyle

from reportlab.lib import colors

from reportlab.lib.pagesizes import (
    letter
)

from datetime import datetime

from reportlab.platypus import KeepTogether



from reportlab.lib.units import mm

def add_page_number(canvas, doc):

        canvas.saveState()

        canvas.setFont("Helvetica-Bold", 9)

        canvas.drawString(
            40,
            770,
            "AI Event Intelligence Report"
        )

        canvas.setFont("Helvetica", 9)

        canvas.drawRightString(
            560,
            20,
            f"Page {canvas.getPageNumber()}"
        )

        canvas.restoreState()

def generate_budget_chart(
        budget_plan,
        output_file
    ):

        labels = []
        values = []

        for key, value in budget_plan.items():

            if key in [
                "remaining_budget",
                "reserve_cost",
                "total_estimated_cost",
                "tool_recommendation",
                "error"
            ]:
                continue

            if isinstance(value, (int, float)):

                labels.append(
                    key.replace("_", " ").title()
                )

                values.append(value)

        plt.figure(figsize=(6,6))

        plt.pie(
            values,
            labels=labels,
            autopct="%1.1f%%"
        )

        plt.title(
            "Budget Allocation"
        )

        plt.savefig(output_file)

        plt.close()

def generate_pdf(
        event_data,
        file_path
    ):

        doc = SimpleDocTemplate(
        file_path,
        pagesize=letter,
        leftMargin=40,
        rightMargin=40,
        topMargin=40,
        bottomMargin=40
    )

        styles = getSampleStyleSheet()
        sectionStyle = ParagraphStyle(
                "SectionStyle",
                parent=styles["Heading2"],
                fontSize=18,
                fontName="Helvetica-Bold",
                leading=20,
                textColor=colors.HexColor("#312E81"),
                spaceBefore=12,
                spaceAfter=12
            )
    
        timelineStyle = ParagraphStyle(
            "TimelineStyle",
            parent=styles["BodyText"],
            leftIndent=20,
            spaceAfter=5,
            fontSize=10
        )
    
        bodyStyle = ParagraphStyle(
            "BodyStyle",
            parent=styles["BodyText"],
            fontSize=10,
            leading=16,
            textColor=colors.HexColor("#374151"),
            spaceAfter=6
        )


        def add_section_divider(elements):

            divider = Table(
                [[""]],
                colWidths=[520],
                rowHeights=[2]
            )

            divider.setStyle(
                TableStyle([
                    ("BACKGROUND",
                    (0,0),
                    (-1,-1),
                    colors.HexColor("#6D28D9"))
                ])
            )

            elements.append(divider)
            elements.append(Spacer(1,8))

        elements = []

        # ==================================
        # DYNAMIC READINESS CALCULATION
        # ==================================

        readiness_score = event_data.get(
            "readiness_score",
            0
        )

        if event_data.get("venue"):
            readiness_score += 20

        if (
            event_data.get("budget_plan")
            or event_data.get("budgetPlan")
        ):
            readiness_score += 20

        if event_data.get("security"):
            readiness_score += 20

        if event_data.get("vendors"):
            readiness_score += 20

        if event_data.get("timeline"):
            readiness_score += 20

        if readiness_score >= 90:
            overall_status = "READY FOR EXECUTION"

        elif readiness_score >= 70:
            overall_status = "PLANNING IN PROGRESS"

        else:
            overall_status = "REQUIRES ATTENTION"

        event_date = (
            event_data.get("eventDate")
            or event_data.get("event_date")
        )

        formatted_date = "N/A"

        if event_date:
            try:
                formatted_date = datetime.strptime(
                    event_date,
                    "%Y-%m-%d"
                ).strftime("%d %B %Y")
            except:
                formatted_date = event_date

        event_name = (
            event_data.get("eventName")
            or event_data.get("event_name")
            or "Event"
        )
        event_type = (
            (event_data.get("eventType") or "").title()
            or event_data.get("event_type")
            or "Event"
        ).title()
            


    # =========================
    # TITLE
    # =========================

        titleStyle = ParagraphStyle(
            "TitleStyle",
            parent=styles["Title"],
            fontSize=24,
            textColor=colors.HexColor("#4F46E5"),
            spaceAfter=10
        )
        elements.append(
            Spacer(1,25)
        )

        cover_banner = Table(
            [["EXECUTIVE EVENT REPORT"]],
            colWidths=[500]
        )

        cover_banner.setStyle(
            TableStyle([
                ("BACKGROUND",(0,0),(-1,-1),colors.HexColor("#4F46E5")),
                ("TEXTCOLOR",(0,0),(-1,-1),colors.white),
                ("ALIGN",(0,0),(-1,-1),"CENTER"),
                ("FONTNAME",(0,0),(-1,-1),"Helvetica-Bold"),
                ("FONTSIZE",(0,0),(-1,-1),18),
                ("TOPPADDING",(0,0),(-1,-1),8),
                ("BOTTOMPADDING",(0,0),(-1,-1),8),
            ])
        )

        elements.append(cover_banner)
        elements.append(Spacer(1,20))

        event_type = (
            (event_data.get("eventType") or "").title()
            or event_data.get("event_type")
            or ""
        ).title()

        frontend_image = event_data.get("image")

        if frontend_image:

            image_name = os.path.basename(
                frontend_image
            )

            event_type = os.path.basename(
                os.path.dirname(frontend_image)
            )

        BASE_DIR = os.path.dirname(
            os.path.dirname(__file__)
        )


        print("PDF IMAGE:")
        print(event_data.get("image"))


        frontend_image = event_data.get("image")

        event_image = None

        if frontend_image:

            image_name = os.path.basename(
                frontend_image
            )

            event_image = os.path.join(
                BASE_DIR,
                "assets",
                event_type,
                image_name
            )


            print("=" * 50)
            print("EVENT TYPE:", event_type)
            print("IMAGE NAME:", image_name)
            print("FULL PATH:", event_image)
            print("FILE EXISTS:", os.path.exists(event_image))
            print("=" * 50)

            print("FILE EXISTS:")
            print(os.path.exists(event_image))
            
        print("=" * 50)
        print("PDF IMAGE:")
        print(frontend_image)
        print("=" * 50)

        print("=" * 50)
        print("EVENT IMAGE:")
        print(event_image)
        print("=" * 50)

        elements.append(
            Paragraph(
                event_name,
                ParagraphStyle(
                    "CoverTitle",
                    parent=styles["Title"],
                    fontSize=24,
                    spaceAfter=10,
                    textColor=colors.HexColor("#4F46E5"),
                    alignment=1
                )
            )
        )

        elements.append(
            Spacer(1,10)
        )

        elements.append(
            Paragraph(
                "Strategic Planning • Budget Intelligence • Vendor Management • Event Readiness",
                ParagraphStyle(
                    "Tagline",
                    parent=styles["BodyText"],
                    alignment=1,
                    textColor=colors.HexColor("#6B7280"),
                    fontSize=9
                )
            )
        )

        cover_info_table = Table(
        [
        ["Client",
            event_data.get("customer_name")
            or event_data.get("customerName")
            or "N/A"],
        ["Date", formatted_date],
        ["Location", event_data.get("location","N/A")],
        ["Guests", str(event_data.get("guests",0))],
        ["Budget", f"Rs. {event_data.get('budget',0):,}"]
        ],
        colWidths=[120,350]
        )
        cover_info_table.hAlign = "CENTER"

        cover_info_table.setStyle(
        TableStyle([
        ("BACKGROUND",(0,0),(0,-1),colors.HexColor("#EEF2FF")),
        ("FONTNAME",(0,0),(0,-1),"Helvetica-Bold"),
        ("GRID",(0,0),(-1,-1),0.5,colors.HexColor("#D1D5DB"))
        ])
        )

        elements.append(cover_info_table)

        elements.append(
            Spacer(1,15)
        )

        status_box = Table(
        [[f"EVENT STATUS : {overall_status}"]],
        colWidths=[500]
        )

        status_box.setStyle(
        TableStyle([
        ("BACKGROUND",(0,0),(-1,-1),colors.HexColor("#10B981")),
        ("TEXTCOLOR",(0,0),(-1,-1),colors.white),
        ("ALIGN",(0,0),(-1,-1),"CENTER"),
        ("TOPPADDING",(0,0),(-1,-1),6),
        ("BOTTOMPADDING",(0,0),(-1,-1),6),
        ("FONTNAME",(0,0),(-1,-1),"Helvetica-Bold"),
        ("FONTSIZE",(0,0),(-1,-1),12)
        ])
        )

        status_box.hAlign = "CENTER"

        elements.append(status_box)
        elements.append(Spacer(1,8))

        elements.append(
            Paragraph(
                "Executive Dashboard",
                sectionStyle
            )
        )

        executive_table = Table(
        [
        ["Metric","Value"],
        ["Event Type", event_type],
        ["Guests", str(event_data.get("guests",0))],
        ["Budget", f"Rs. {event_data.get('budget',0):,}"],
        ["Readiness Score", f"{readiness_score}%"]
        ],
        colWidths=[220,280]
        )
        executive_table.hAlign = "CENTER"

        executive_table.setStyle(
        TableStyle([
        ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#4F46E5")),
        ("TEXTCOLOR",(0,0),(-1,0),colors.white),
        ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),
        ("GRID",(0,0),(-1,-1),0.5,colors.HexColor("#D1D5DB"))
        ])
        )

        elements.append(executive_table)

        elements.append(
            Spacer(1,15)
        )

        dashboard_title = Paragraph(
            "Event Readiness Dashboard",
            sectionStyle
        )

        elements.append(dashboard_title)

        dashboard_rows = [
            ["Metric", "Status"],
            [
                "Venue",
                "✓ Ready" if event_data.get("venue") else "Pending"
            ],
            [
                "Budget",
                "✓ Approved" if event_data.get("budget_plan") else "Pending"
            ],
            [
                "Security",
                "✓ Planned" if event_data.get("security") else "Pending"
            ],
            [
                "Vendors",
                f"{len(event_data.get('vendors',[]))} Vendors"
            ],
            [
                "Timeline",
                "✓ Prepared" if event_data.get("timeline") else "Pending"
            ]
        ]

        dashboard_rows.append(
            ["Overall Status", overall_status]
        )
        dashboard_rows.append(
        [
            "Readiness Score",
            f"{readiness_score}%"
        ]
    )

        dashboard_table = Table(
            dashboard_rows,
            colWidths=[220,280]
        )

        elements.append(Spacer(1,8))

        budget = float(event_data.get("budget",0) or 0)
        guests = int(event_data.get("guests",1) or 1)

        budget_per_guest = budget / max(guests,1)

        kpi_table = Table([
            ["KPI","Value"],
            ["Expected Guests", str(guests)],
            ["Budget Per Guest", f"Rs. {budget_per_guest:,.0f}"],
            ["Vendor Count", str(len(event_data.get("vendors",[])))],
            ["Readiness Score", f"{readiness_score}%"],
            ["Event Type", event_type]
        ],
        colWidths=[180,180]
        )

        kpi_table.setStyle(TableStyle([
            ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#4F46E5")),
            ("TEXTCOLOR",(0,0),(-1,0),colors.white),
            ("GRID",(0,0),(-1,-1),0.5,colors.HexColor("#D1D5DB"))
        ]))
        


        dashboard_table.setStyle(
        TableStyle([
        ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#4F46E5")),
        ("TEXTCOLOR",(0,0),(-1,0),colors.white),
        ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),
        ("GRID",(0,0),(-1,-1),0.5,colors.HexColor("#D1D5DB")),
        ("ROWBACKGROUNDS",(0,1),(-1,-1),
        [
        colors.white,
        colors.HexColor("#F9FAFB")
        ])
        ])
        )

        elements.append(dashboard_table)

        elements.append(
            Paragraph(
                f"<b>Overall Event Readiness Score: {readiness_score}%</b>",
                bodyStyle
            )
        )
        progress_width = (470 * readiness_score) / 100

        progress_bar = Table(
            [[""]],
            colWidths=[progress_width],
            rowHeights=[10]
        )
        

        progress_bar.setStyle(
        TableStyle([
        ("BACKGROUND",(0,0),(-1,-1),
        colors.HexColor("#22C55E"))
        ])
        )

        elements.append(progress_bar)

        elements.append(
            Spacer(1,10)
        )

        kpi_table.hAlign = "CENTER"

        elements.append(PageBreak())

        elements.append(
            Paragraph(
                "Key Performance Indicators",
                sectionStyle
            )
        )

        elements.append(
            Spacer(1,8)
        )

        elements.append(kpi_table)

        elements.append(
            Spacer(1,15)
        )

        
        visual_header = Table(
            [[f"{event_name} - Event Preview"]],
            colWidths=[520]
        )

        visual_header.setStyle(
            TableStyle([
                ("BACKGROUND",(0,0),(-1,-1),
                colors.HexColor("#4F46E5")),

                ("TEXTCOLOR",(0,0),(-1,-1),
                colors.white),

                ("ALIGN",(0,0),(-1,-1),
                "CENTER"),

                ("FONTNAME",(0,0),(-1,-1),
                "Helvetica-Bold")
            ])
        )

        elements.append(visual_header)
        elements.append(Spacer(1,5))

        elements.append(
            Paragraph(
                "Event Visualization",
                sectionStyle
            )
        )

        elements.append(
                Spacer(
                    1,
                    15
                )
            )

        elements.append(
            Paragraph(
                f"""
                AI generated event visualization for
                <b>{event_name}</b>
                based on submitted event requirements.
                """,
                bodyStyle
            )
        )

        elements.append(
            Spacer(1,10)
        )

        elements.append(
            Spacer(1,20)
        )

        if event_image and os.path.exists(event_image):

            try:

                print("=" * 50)
                print("ADDING IMAGE TO PDF")
                print(event_image)
                print(os.path.exists(event_image))
                print("=" * 50)
                
                event_img = Image(
                    event_image,
                    width=420,
                    height=240
                )

                event_img.hAlign = "CENTER"

                elements.append(event_img)

                elements.append(
                    Spacer(1,10)
                )

                elements.append(
                    Paragraph(
                        "AI Generated Event Preview",
                        styles["Heading3"]
                    )
                )

                elements.append(
                    Paragraph(
                        f"""
                        This visualization represents the proposed atmosphere,
                        event styling, guest experience, and overall theme for
                        <b>{event_name}</b>.
                        """,
                        bodyStyle
                    )
                )

                stats_table = Table(
                [
                ["Theme", event_data.get("vibe","N/A")],
                ["Guests", str(event_data.get("guests",0))],
                ["Budget", f"Rs. {event_data.get('budget',0):,}"],
                ["Location", event_data.get("location","N/A")]
                ],
                colWidths=[120,350]
                )

                stats_table.setStyle(
                TableStyle([
                ("BACKGROUND",(0,0),(0,-1),colors.HexColor("#EEF2FF")),
                ("FONTNAME",(0,0),(0,-1),"Helvetica-Bold"),
                ("GRID",(0,0),(-1,-1),0.5,colors.HexColor("#D1D5DB"))
                ])
                )

                elements.append(stats_table)

                elements.append(
                    Spacer(1,5)
                )

                

            except Exception as e:
                print(e)

        header_box = Table(
            [[event_name]],
            colWidths=[520]
        )

        header_box.setStyle(
            TableStyle([
                ("BACKGROUND",(0,0),(-1,-1),colors.HexColor("#4F46E5")),
                ("TEXTCOLOR",(0,0),(-1,-1),colors.white),
                ("ALIGN",(0,0),(-1,-1),"CENTER"),
                ("FONTNAME",(0,0),(-1,-1),"Helvetica-Bold"),
                ("FONTSIZE",(0,0),(-1,-1),16),
                ("TOPPADDING",(0,0),(-1,-1),12),
                ("BOTTOMPADDING",(0,0),(-1,-1),12),
            ])
        )

        elements.append(header_box)

        summary_box = Table(
        [
        ["Event", event_name],
        ["Location", event_data.get("location","N/A")],
        ["Guests", str(event_data.get("guests",0))],
        ["Budget", f"Rs. {event_data.get('budget',0):,}"]
        ],
        colWidths=[170,330]
        )

        summary_box.setStyle(
        TableStyle([
        ("BACKGROUND",(0,0),(0,-1),colors.HexColor("#EEF2FF")),
        ("FONTNAME",(0,0),(0,-1),"Helvetica-Bold"),
        ("GRID",(0,0),(-1,-1),0.5,colors.HexColor("#E5E7EB")),
        ("TOPPADDING",(0,0),(-1,-1),8),
        ("BOTTOMPADDING",(0,0),(-1,-1),8),
        ("BOX",(0,0),(-1,-1),1,colors.HexColor("#D1D5DB"))
        ])
        )

        elements.append(summary_box)
        elements.append(Spacer(1,15))

        event_type = (
            (event_data.get("eventType") or "").title()
            or event_data.get("event_type")
            or "Event"
        ).title()

        elements.append(
            Paragraph(
                f"{event_type} Event Proposal",
                styles["Heading2"]
            )
        )

        elements.append(
            Spacer(1,10)
        )


    # EXECUTIVE SUMMARY


        classification = event_data.get(
            "classification",
            {}
        )

        event_scale = classification.get(
            "event_scale",
            "Medium Scale"
        )

        priority = classification.get(
            "priority",
            "Standard"
        )

        elements.append(
            Paragraph(
                "Executive Summary",
                sectionStyle
            )
        )

        elements.append(
            Paragraph(
                f"""
                <b>Executive Status:</b> {overall_status}<br/>
                <b>Event Scale:</b> {event_scale}<br/>

                <b>Priority:</b> {priority}
                """,
                bodyStyle
            )
        )
        add_section_divider(elements)

        elements.append(
            Paragraph(
            f"""
            This report presents a comprehensive plan for
            <b>{event_name}</b>, a
            <b>{event_type}</b> event scheduled at
            <b>{event_data.get('location','N/A')}</b>.

            The plan has been prepared for approximately
            <b>{event_data.get('guests',0)}</b> guests
            with a budget allocation of
            <b>Rs. {event_data.get('budget',0):,}</b>.

            The report includes venue planning,
            vendor coordination, guest experience strategy,
            security preparation, entertainment planning,
            and execution readiness recommendations.
            """,
            bodyStyle
            )
        )

        elements.append(
            Spacer(1,15)
        )
        event_type = (
            (event_data.get("eventType") or "").title()
            or event_data.get("event_type")
            or "Event"
        ).title()

        duration = (
            event_data.get("event_duration")
            or event_data.get("eventDuration")
            or event_data.get("duration")
            or "Full Day"
        )

        event_name = (
            event_data.get("eventName")
            or event_data.get("event_name")
            or "Event"
        )

        elements.append(
            Paragraph(
                "Event Overview",
                sectionStyle
            )
        )
        add_section_divider(elements)

        overview_table = Table(
        [
        ["Event Name", event_name],
        ["Event Type", event_type],
        ["Date", formatted_date],
        ["Duration", duration],
        ["Guests", str(event_data.get("guests",0))],
        ["Location", event_data.get("location","N/A")],
        ["Budget", f"Rs. {event_data.get('budget',0):,}"]
        ],
        colWidths=[180,300]
        )

        overview_table.setStyle(
        TableStyle([
        ("BACKGROUND",(0,0),(0,-1),colors.HexColor("#EEF2FF")),
        ("FONTNAME",(0,0),(0,-1),"Helvetica-Bold"),

        ("GRID",(0,0),(-1,-1),0.5,colors.HexColor("#E5E7EB")),

        ("LINEBELOW",(0,0),(-1,-1),0.3,colors.HexColor("#E5E7EB")),

        ("LEFTPADDING",(0,0),(-1,-1),10),
        ("TOPPADDING",(0,0),(-1,-1),8),
        ("BOTTOMPADDING",(0,0),(-1,-1),8),
        ])
        )
        elements.append(overview_table)
        elements.append(Spacer(1,20))


        elements.append(
        Paragraph(
            f"""
            {event_name} is a premium
            {event_type} planned for
            approximately {event_data.get('guests')} guests
            at {event_data.get('location')}.

            This event has been designed with a strong focus
            on guest experience, venue excellence, security,
            catering, entertainment and operational execution.

            The allocated budget of
            Rs. {event_data.get('budget',0):,}
            has been strategically distributed to ensure
            a seamless and memorable event experience.
            """,
            bodyStyle
        )
    )

        elements.append(
            Spacer(1,15)
        )   



        elements.append(
            Paragraph(
                "Event Vision",
                sectionStyle
            )
        )
        add_section_divider(elements)

        vision_box = Table(
            [
                [
                    Paragraph(
                        f"""
                        <b>Vision</b><br/><br/>

                        To create a memorable
                        {event_type.lower()} experience for
                        approximately {event_data.get('guests',0)}
                        attendees through a
                        {event_data.get('vibe','premium')}
                        atmosphere, strategic planning,
                        high-quality vendors,
                        and seamless execution.
                        """,
                        bodyStyle
                    )
                ]
            ],
            colWidths=[520]
        )

        vision_box.setStyle(
            TableStyle([
                ("BACKGROUND",(0,0),(-1,-1),colors.HexColor("#F8FAFC")),
                ("BOX",(0,0),(-1,-1),1,colors.HexColor("#E5E7EB")),
                ("LEFTPADDING",(0,0),(-1,-1),12),
                ("RIGHTPADDING",(0,0),(-1,-1),12),
                ("TOPPADDING",(0,0),(-1,-1),10),
                ("BOTTOMPADDING",(0,0),(-1,-1),10),
            ])
        )

        elements.append(vision_box)


        theme_box = Table(
            [
            [
            Paragraph(
            f"""
            <b>Event Theme</b><br/>
            {
            event_data.get("theme")
            or event_data.get("vibe")
            or event_type
            }
            """,
            bodyStyle
            )
            ]
            ],
            colWidths=[520]
            )

        theme_box.setStyle(
            TableStyle([
            ("BACKGROUND",(0,0),(-1,-1),
            colors.HexColor("#EEF2FF")),
            ("BOX",(0,0),(-1,-1),1,
            colors.HexColor("#4F46E5"))
            ])
            )

        elements.append(theme_box)
        elements.append(Spacer(1,10))
        elements.append(
            Spacer(1,15)
        )

        venue_data = event_data.get("venue", {})

        if isinstance(venue_data, dict):
            venue_name = (
            venue_data.get("venue_name")
            or event_data.get("venueName")
            or "Venue To Be Finalized"
        )
            
        else:
            venue_name = str(venue_data)

        requirements = event_data.get(
            "requirements",
            ""
        )

        if requirements:

            elements.append(
                Paragraph(
                    "Client Requirements",
                    sectionStyle
                )
            )
            add_section_divider(elements)

            req_rows = []

            for req in requirements.split(","):
                req_rows.append(
                    [f"• {req.strip()}"]
                )

            req_table = Table(
                req_rows,
                colWidths=[500]
            )

            req_table.setStyle(
                TableStyle([
                    ("BOX",(0,0),(-1,-1),1,
                    colors.HexColor("#E5E7EB")),

                    ("ROWBACKGROUNDS",
                    (0,0),
                    (-1,-1),
                    [
                        colors.white,
                        colors.HexColor("#F9FAFB")
                    ])
                ])
            )

            elements.append(req_table)
            elements.append(Spacer(1,15))

        # =========================
        # VENUE PLAN
        # =========================

        venue = event_data.get(
            "venue",
            {}
        )

        if isinstance(
            venue,
            dict
        ):

            elements.append(

                Paragraph(
                    "Venue Plan",
                    sectionStyle
                )
            )
            add_section_divider(elements)


            elements.append(
                Spacer(1, 10)
            )

            venue_rows = [
            ["Attribute","Details"]
            ]

            for key, value in venue.items():

                if key in ["tool_recommendation", "error"]:
                    continue

                venue_rows.append([
                    key.replace("_"," ").title(),
                    str(value)
                ])

            venue_table = Table(
                venue_rows,
                colWidths=[180,300]
            )

            venue_table.setStyle(
                TableStyle([
                    ("LINEBELOW",(0,0),(-1,-1),0.3,colors.HexColor("#D1D5DB")),

                    ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#4F46E5")),

                    ("TEXTCOLOR",(0,0),(-1,0),colors.white),

                    ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),

                    ("BACKGROUND",(0,1),(0,-1),colors.HexColor("#F3F4F6")),

                    ("FONTNAME",(0,1),(0,-1),"Helvetica-Bold"),

                    ("ROWBACKGROUNDS",
                        (0,1),
                        (-1,-1),
                        [
                        colors.white,
                        colors.HexColor("#F9FAFB")
                        ]),
                ])
            )

            elements.append(venue_table)
            elements.append(Spacer(1,20))
        # =========================
        # FOOD PLAN
        # =========================

        food = event_data.get(
            "food",
            {}
        )

        print("=" * 80)
        print("PDF FOOD DATA")
        print(food)
        print("=" * 80)

        if food:

            elements.append(PageBreak())

            elements.append(
                Paragraph(
                    "Food Plan",
                    sectionStyle
                )
            )

            add_section_divider(elements)

            elements.append(
                Spacer(1, 10)
            )

            for key, value in food.items():

                if key in ["tool_recommendation", "error"]:
                    continue


                if isinstance(value, list):

                    elements.append(
                        Paragraph(
                            f"<b>{key.replace('_',' ').title()}</b>",
                            styles["Heading4"]
                        )
                    )

                    for item in value[:1]:

                        elements.append(
                            Paragraph(
                                f"• {item[:80]}",
                                styles["BodyText"]
                            )
                        )

                else:

                    elements.append(
                        Paragraph(
                            f"<b>{key.replace('_',' ').title()}:</b> {value}",
                            styles["BodyText"]
                        )
                    )


            

            elements.append(
                Spacer(1, 15)
            )

        # =========================
        # DECORATION PLAN
        # =========================

        decoration = event_data.get(
            "decoration",
            {}
        )

        print("=" * 80)
        print("PDF DECORATION DATA")
        print(decoration)
        print("=" * 80)

        if decoration:

            elements.append(

                Paragraph(
                    "Decoration Plan",
                    sectionStyle
                )
            )
            add_section_divider(elements)

            elements.append(
                Spacer(1, 10)
            )

            for key, value in decoration.items():

                if key in ["tool_recommendation", "error"]:
                    continue

                elements.append(

                    Paragraph(

                        f"<b>{key.replace('_',' ').title()}:</b> {value}",

                        styles["BodyText"]
                    )
                )

            elements.append(
                Spacer(1, 15)
            )

        # =========================
        # SECURITY PLAN
        # =========================

        security = event_data.get(
            "security",
            {}
        )

        if security:

            elements.append(

                Paragraph(
                    "Security Plan",
                    sectionStyle
                )
            )
            add_section_divider(elements)

            elements.append(
                Spacer(1, 10)
            )

            for key, value in security.items():

                if key == "risk_alert":
                    continue

                if key in [
                    "tool_recommendation",
                    "error"
                ]:
                    continue

                elements.append(

                    Paragraph(

                        f"<b>{key.replace('_',' ').title()}:</b> {value}",

                        styles["BodyText"]
                    )
                )

            elements.append(
                Spacer(1, 15)
            )

        # =========================
        # ENTERTAINMENT PLAN
        # =========================

        entertainment = event_data.get(
            "entertainment",
            {}
        )

        print("=" * 80)
        print("PDF ENTERTAINMENT DATA")
        print(entertainment)
        print("=" * 80)

        

        if entertainment:
            elements.append(PageBreak())

            elements.append(

                Paragraph(
                    "Entertainment Plan",
                    sectionStyle
                )
                
            )
            add_section_divider(elements)

            elements.append(
                    Paragraph(
                        "Entertainment experiences curated for guest engagement and event success.",
                        styles["Italic"]
                    )
            )

            elements.append(
                Spacer(1,10)
            )

            elements.append(
                Spacer(1, 10)
            )

            for key, value in entertainment.items():

                if key in [
                    "tool_recommendation",
                    "error"
                ]:
                    continue

                if isinstance(value, list):
                    value = ", ".join(value)

                elements.append(
                    Paragraph(
                        f"<b>{key.replace('_',' ').title()}:</b> {value}",
                        styles["BodyText"]
                    )
                )

                elements.append(Spacer(1,15))

            entertainment_summary = Table(
            [
            [
            Paragraph(
            f"""
            <b>Entertainment Strategy Summary</b><br/><br/>

            The entertainment program has been designed to maximize
            guest engagement, create memorable experiences,
            maintain audience participation throughout the event,
            and support the overall event theme and atmosphere.

            Special attention has been given to stage activities,
            interactive experiences, audience involvement,
            and seamless coordination between performances.
            """,
            bodyStyle
            )
            ]
            ],
            colWidths=[520]
            )

            entertainment_summary.setStyle(
            TableStyle([
            ("BACKGROUND",(0,0),(-1,-1),colors.HexColor("#F8FAFC")),
            ("BOX",(0,0),(-1,-1),1,colors.HexColor("#D1D5DB")),
            ("LEFTPADDING",(0,0),(-1,-1),10),
            ("RIGHTPADDING",(0,0),(-1,-1),10),
            ("TOPPADDING",(0,0),(-1,-1),10),
            ("BOTTOMPADDING",(0,0),(-1,-1),10)
            ])
            )

            elements.append(entertainment_summary)

            elements.append(Spacer(1,20))


            entertainment_kpi = Table(
            [
            ["Entertainment Metric","Status"],
            ["Guest Engagement","High"],
            ["Audience Interaction","Planned"],
            ["Stage Coordination","Ready"],
            ["Performance Flow","Optimized"],
            ["Experience Quality","Premium"]
            ],
            colWidths=[250,220]
            )

            entertainment_kpi.setStyle(
            TableStyle([
            ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#4F46E5")),
            ("TEXTCOLOR",(0,0),(-1,0),colors.white),
            ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),
            ("GRID",(0,0),(-1,-1),0.5,colors.HexColor("#D1D5DB"))
            ])
            )

            elements.append(entertainment_kpi)

            elements.append(
                Spacer(1, 15)
            )

        # =========================
        # BUDGET BREAKDOWN
        # =========================

        budget_plan = (
            event_data.get("budget_plan")
            or event_data.get("budgetPlan")
            or {}
        )

        chart_path = os.path.join(
            BASE_DIR,
            "budget_chart.png"
        )

        print("Chart Path:", chart_path)
        print("Budget Plan:", budget_plan)

        if budget_plan:

            generate_budget_chart(
                budget_plan,
                chart_path
            )

            print(
                os.path.exists(
                    chart_path
                )
            )

        if budget_plan:

            elements.append(PageBreak())

            elements.append(

                Paragraph(
                    "Budget Breakdown",
                    sectionStyle
                )
            )
            add_section_divider(elements)

            total_budget = float(event_data.get("budget",0) or 0)

            allocated = (
                total_budget
                -
                budget_plan.get("remaining_budget",0)
            )

            elements.append(
                Paragraph(
                    f"""
                    <b>Allocated Budget:</b>
                    Rs. {allocated:,.0f}<br/>

                    <b>Reserve Budget:</b>
                    Rs. {budget_plan.get('remaining_budget',0):,.0f}
                    """,
                    styles["BodyText"]
                )
            )

            elements.append(Spacer(1,15))
            summary_table = Table(
            [
            ["Total Budget", f"Rs. {event_data.get('budget',0):,}"],
            ["Allocated", f"Rs. {allocated:,.0f}"],
            ["Reserve", f"Rs. {budget_plan.get('remaining_budget',0):,.0f}"]
            ],
            colWidths=[180,180]
            )

            summary_table.setStyle(
            TableStyle([
                ("LINEBELOW",(0,0),(-1,-1),0.3,colors.HexColor("#D1D5DB")),
                ("BACKGROUND",(0,0),(0,-1),colors.HexColor("#EDE9FE")),
                ("FONTNAME",(0,0),(0,-1),"Helvetica-Bold")
            ])
            )

            elements.append(summary_table)

            elements.append(
                Spacer(1, 10)
            )


            elements.append(
                Paragraph(
                    f"""
                    <b>Total Event Budget:</b>
                    Rs. {event_data.get('budget',0):,}
                    """,
                    styles["Heading3"]
                )
            )

            elements.append(
                Spacer(1,10)
            )

            budget_rows = [
                ["Category", "Amount"]
            ]

            for key, value in budget_plan.items():

                if key in [
                    "error",
                    "tool_recommendation",
                    "reserve_cost",
                    "remaining_budget",
                    "total_estimated_cost"
                ]:
                    continue

                if isinstance(value, (int, float)):

                    percentage = (
                        value / max(total_budget,1)
                    ) * 100

                    amount = (
                        f"Rs. {int(value):,}"
                        f" ({percentage:.1f}%)"
                    )

                else:

                    amount = str(value)

                budget_rows.append([
                    key.replace("_"," ").title(),
                    amount
                ])

            budget_table = Table(
                    budget_rows,
                    colWidths=[240,220]
                )

            budget_table.setStyle(
                TableStyle([

                    ("LINEBELOW",(0,0),(-1,-1),0.3,colors.HexColor("#D1D5DB")),

                    ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#4F46E5")),

                    ("TEXTCOLOR",(0,0),(-1,0),colors.white),

                    ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),

                    ("BACKGROUND",(0,1),(0,-1),colors.HexColor("#F5F7FA")),

                    ("ALIGN",(1,1),(1,-1),"RIGHT"),

                    ("PADDING",(0,0),(-1,-1),8),

                    ("VALIGN",(0,0),(-1,-1),"MIDDLE")
                ])
            )

            elements.append(budget_table)

            if os.path.exists(chart_path):

                elements.append(
                    Spacer(1,15)
                )

                chart_img = Image(
                    chart_path,
                    width=280,
                    height=280
                )

                chart_img.hAlign = "CENTER"

                budget_analysis = [
                    Paragraph(
                        "Budget Allocation Analysis",
                        styles["Heading3"]
                    ),
                    chart_img,
                    Paragraph(
                        f"""
                        <b>Budget Insight:</b>
                        Estimated spend per attendee:
                        Rs. {budget_per_guest:,.0f}
                        """,
                        bodyStyle
                    )
                ]

                elements.append(
                    KeepTogether(
                        budget_analysis
                    )
                )

           
            elements.append(PageBreak())

            timeline_section = []
            print("PAGE BREAK BEFORE TIMELINE")

            

        # =========================
        # TIMELINE
        # =========================
        print("=" * 60)
        print("TIMELINE DATA RECEIVED IN PDF")
        print(event_data.get("timeline"))
        print("=" * 60)

        print("=" * 60)
        print("EVENT DURATION IN PDF")
        print(
            event_data.get("duration")
            or event_data.get("eventDuration")
            or event_data.get("event_duration")
        )
        print("=" * 60)



        timeline = event_data.get("timeline", {})

        if timeline and isinstance(timeline, dict):

            elements.append(
                Paragraph(
                    "Detailed Event Execution Timeline",
                    sectionStyle
                )
            )

            elements.append(
                Paragraph(
                    f"Duration: {duration}",
                    bodyStyle
                )
            )

            events = timeline.get("event", [])

            if events:

                # MULTI DAY FORMAT
                if isinstance(events[0], dict) and "activities" in events[0]:

                    for index, day_data in enumerate(events):

                        if index > 0:
                            elements.append(PageBreak())

                            elements.append(
                                Paragraph(
                                    "Detailed Event Execution Timeline",
                                    sectionStyle
                                )
                            )

                            elements.append(
                                Paragraph(
                                    f"Duration: {duration}",
                                    bodyStyle
                                )
                            )

                            elements.append(Spacer(1,10))

                        elements.append(
                            Paragraph(
                                day_data.get("day", "Schedule"),
                                styles["Heading2"]
                            )
                        )


                        rows = [["Time", "Activity"]]


                        elements.append(
                            Paragraph(
                                f"Total Activities: {len(day_data.get('activities', []))}",
                                bodyStyle
                            )
                        )
                        elements.append(Spacer(1, 15))

                        for item in day_data.get("activities", []):

                            rows.append([
                                item.get("time", ""),
                                item.get("activity", "")
                            ])

                        table = Table(
                            rows,
                            colWidths=[120,350]
                        )

                        table.setStyle(
                            TableStyle([
                                ("BACKGROUND",(0,0),(-1,0),
                                colors.HexColor("#4F46E5")),
                                ("TEXTCOLOR",(0,0),(-1,0),
                                colors.white),
                                ("GRID",(0,0),(-1,-1),
                                0.5,
                                colors.black)
                            ])
                        )

                        elements.append(table)
                        

                        elements.append(Spacer(1,15))

                        activities = day_data.get("activities", [])

                        total_activities = len(activities)

                        start_time = (
                            activities[0].get("time", "N/A")
                            if activities else "N/A"
                        )

                        end_time = (
                            activities[-1].get("time", "N/A")
                            if activities else "N/A"
                        )

                        summary_table = Table(
                        [
                            ["Timeline Summary", ""],
                            ["Start Time", start_time],
                            ["End Time", end_time],
                            ["Total Activities", str(total_activities)],
                            ["Execution Status", "Ready"]
                        ],
                        colWidths=[180,250]
                        )

                        summary_table.setStyle(
                        TableStyle([
                            ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#4F46E5")),
                            ("TEXTCOLOR",(0,0),(-1,0),colors.white),
                            ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),
                            ("GRID",(0,0),(-1,-1),0.5,colors.HexColor("#D1D5DB"))
                        ])
                        )

                        elements.append(summary_table)

                        elements.append(Spacer(1,10))

                        elements.append(
                            Paragraph(
                                f"""
                                <b>Operational Notes</b><br/>
                                • Total scheduled activities: {total_activities}.<br/>
                                • Event execution begins at {start_time}.<br/>
                                • Final scheduled activity concludes at {end_time}.<br/>
                                • Timeline has been optimized for smooth event operations.
                                """,
                                bodyStyle
                            )
                        )

                        elements.append(Spacer(1,15))

                # SINGLE DAY FORMAT
                else:

                    rows = [["Time", "Activity"]]

                    for item in events:

                        rows.append([
                            item.get("time", ""),
                            item.get("activity", "")
                        ])

                    table = Table(
                        rows,
                        colWidths=[120,350]
                    )

                    table.setStyle(
                        TableStyle([
                            ("BACKGROUND",(0,0),(-1,0),
                            colors.HexColor("#4F46E5")),
                            ("TEXTCOLOR",(0,0),(-1,0),
                            colors.white),
                            ("GRID",(0,0),(-1,-1),
                            0.5,
                            colors.black)
                        ])
                    )

                    elements.append(table)

                    elements.append(Spacer(1,15))

                    total_activities = len(events)

                    start_time = (
                        events[0].get("time", "N/A")
                        if events else "N/A"
                    )

                    end_time = (
                        events[-1].get("time", "N/A")
                        if events else "N/A"
                    )

                    summary_table = Table(
                    [
                        ["Timeline Summary", ""],
                        ["Start Time", start_time],
                        ["End Time", end_time],
                        ["Total Activities", str(total_activities)],
                        ["Execution Status", "Ready"]
                    ],
                    colWidths=[180,250]
                    )

                    summary_table.setStyle(
                    TableStyle([
                        ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#4F46E5")),
                        ("TEXTCOLOR",(0,0),(-1,0),colors.white),
                        ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),
                        ("GRID",(0,0),(-1,-1),0.5,colors.HexColor("#D1D5DB"))
                    ])
                    )

                    elements.append(summary_table)

                    elements.append(Spacer(1,10))

                    elements.append(
                        Paragraph(
                            f"""
                            <b>Operational Notes</b><br/>
                            • Total scheduled activities: {total_activities}.<br/>
                            • Event execution begins at {start_time}.<br/>
                            • Final scheduled activity concludes at {end_time}.<br/>
                            • Timeline has been optimized for smooth event operations.
                            """,
                            bodyStyle
                        )
                    )

                    elements.append(Spacer(1,15))

        
        # =========================
        # VENDOR SUMMARY
        # =========================

        vendors = event_data.get(
            "vendors",
            []
        )


        vendor_rows = [
                ["Vendor Name", "Category", "Rating"]
            ]

        for vendor in vendors[:12]:

                if isinstance(vendor, dict):

                    vendor_rows.append([
                    vendor.get("name", "N/A"),
                    vendor.get("category", "N/A"),
                    str(vendor.get("rating", "N/A"))
                ])

                else:

                    vendor_rows.append([
                        str(vendor),
                        "N/A",
                        "N/A"
                    ])

        if not vendors:
                vendor_rows = [
                    ["Vendor Name","Category","Rating"],
                    ["No Vendors Assigned","N/A","N/A"]
                ]

        vendor_table = Table(
            vendor_rows,
            colWidths=[220,150,80]
        )

        vendor_table.setStyle(
            TableStyle([
                ("BACKGROUND",(0,0),(-1,0),
                colors.HexColor("#4F46E5")),

                ("TEXTCOLOR",(0,0),(-1,0),
                colors.white),

                ("FONTNAME",(0,0),(-1,0),
                "Helvetica-Bold"),

                ("GRID",(0,0),(-1,-1),
                0.5,
                colors.HexColor("#E5E7EB")),

                ("ROWBACKGROUNDS",
                (0,1),
                (-1,-1),
                [
                    colors.white,
                    colors.HexColor("#F9FAFB")
                ])
            ])
        )

        guests = event_data.get("guestsList", [])

        guest_rows = [
            ["Guest Type", "Count"]
        ]

        if guests:

            guest_rows.append([
                "Registered Guests",
                str(len(guests))
            ])

        else:

            guest_rows.append([
                "Expected Guests",
                str(event_data.get("guests", 0))
            ])

        guest_table = Table(
            guest_rows,
            colWidths=[220, 220]
        )

        guest_table.setStyle(
            TableStyle([
                ("BACKGROUND",(0,0),(-1,0),
                colors.HexColor("#4F46E5")),

                ("TEXTCOLOR",(0,0),(-1,0),
                colors.white),

                ("GRID",(0,0),(-1,-1),
                0.5,
                colors.HexColor("#D1D5DB"))
            ])
        )


        operations_highlight_table = Table(
        [
            ["Metric", "Value"],
            ["Event Type", str(event_type)],
            ["Duration", str(duration)],
            ["Expected Guests", str(event_data.get("guests", 0))],
            ["Vendor Count", str(len(event_data.get("vendors", [])))],
            ["Readiness Score", f"{readiness_score}%"]
        ],
        colWidths=[220,220]
        )

        operations_highlight_table.setStyle(
            TableStyle([
                ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#4F46E5")),
                ("TEXTCOLOR",(0,0),(-1,0),colors.white),
                ("GRID",(0,0),(-1,-1),0.5,colors.HexColor("#D1D5DB"))
            ])
        )


        vendor_guest_section = [

            Paragraph(
                "Vendor Summary",
                sectionStyle
            ),

            Paragraph(
                f"Confirmed Vendors: {len(vendors)}",
                styles["Heading4"]
            ),

            Spacer(1,5),

            vendor_table,

            Spacer(1,15),

            Paragraph(
                "Guest Management Summary",
                sectionStyle
            ),

            guest_table,

            Spacer(1,15),


            Paragraph(
                "Operational Highlights",
                sectionStyle
            ),

            operations_highlight_table,

            Spacer(1,15),
        ]

        operations_table = Table(
        [
            ["Operational Metric", "Value"],
            ["Expected Attendance", str(event_data.get("guests", 0))],
            ["Vendor Count", str(len(event_data.get("vendors", [])))],
            ["Event Duration", str(duration)],
            ["Budget Per Guest", f"Rs. {budget_per_guest:,.0f}"],
            ["Event Type", str(event_type)],
            ["Readiness Score", f"{readiness_score}%"]
        ],
        colWidths=[220,220]
        )

        operations_table.setStyle(
            TableStyle([
                ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#4F46E5")),
                ("TEXTCOLOR",(0,0),(-1,0),colors.white),
                ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),
                ("GRID",(0,0),(-1,-1),0.5,colors.HexColor("#D1D5DB")),
                ("ROWBACKGROUNDS",
                    (0,1),
                    (-1,-1),
                    [colors.white, colors.HexColor("#F9FAFB")]
                )
            ])
        )
        elements.append(PageBreak())

        elements.extend(
            vendor_guest_section
        )
        # =========================
        # AI INSIGHTS
        # =========================

        insights = event_data.get(
            "insights",
            []
        )
        if insights:

            elements.append(PageBreak())

            elements.append(
                Paragraph(
                    "AI Insights",
                    sectionStyle
                )
            )
            add_section_divider(elements)

            elements.append(
                Paragraph(
                    "Key observations generated from AI analysis.",
                    styles["Italic"]
                )
            )

            elements.append(
                Spacer(1,10)
            )

            for item in insights[:8]:

                insight_box = Table(
                [
                ["AI Recommendation"],
                [
                Paragraph(
                    str(item),
                    bodyStyle
                )
                ]
                ],
                colWidths=[500]
                )

                insight_box.setStyle(
                TableStyle([
                ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#10B981")),
                ("TEXTCOLOR",(0,0),(-1,0),colors.white),
                ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),

                ("TOPPADDING",(0,1),(-1,-1),8),
                ("BOTTOMPADDING",(0,1),(-1,-1),8),
                ("LEFTPADDING",(0,1),(-1,-1),10),
                ("RIGHTPADDING",(0,1),(-1,-1),10),

                ("GRID",(0,0),(-1,-1),0.5,colors.HexColor("#D1D5DB"))
                ])
                )

                elements.append(insight_box)

                elements.append(
                    Spacer(1,10)
                )

        elements.append(PageBreak())

        elements.append(
            Paragraph(
                "Final Recommendations",
                sectionStyle
            )
        )
        add_section_divider(elements)
        elements.append(
            Spacer(1,10)
        )

        elements.append(
            Paragraph(
                f"""
                Based on the analysis performed by the AI Event Planner,
                the event <b>{event_data.get(
                                'event_name'
                            ) or event_data.get(
                                'eventName',
                                ''
                            )}</b>
                is considered operationally feasible and ready for execution.

                The venue, vendors, security strategy,
                budget allocation and timeline have been optimized
                to maximize attendee experience while maintaining
                operational efficiency and budget control.
                """,
                bodyStyle
            )
        )

        elements.append(
            Spacer(1,15)
        )

        guest_count = int(event_data.get("guests",0))

        recommendations = []

        if event_data.get("vendors"):
            recommendations.append(
                "Finalize vendor agreements"
            )

        if event_data.get("venue"):
            recommendations.append(
                "Conduct venue walkthrough"
            )

        if event_data.get("security"):
            recommendations.append(
                "Review security preparedness"
            )

        if event_data.get("timeline"):
            recommendations.append(
                "Validate event timeline"
            )

        if event_data.get("guests",0) > 100:
            recommendations.append(
                "Strengthen guest management operations"
            )

            if guest_count > 1000:
                recommendations.append(
                    "Deploy advanced crowd control strategy"
                )

            if budget > 1000000:
                recommendations.append(
                    "Perform executive budget review"
                )

        recommendation_text = "<br/>".join(
            [f"• {r}" for r in recommendations]
        )

        elements.append(
            Spacer(1,20)
        )


        elements.append(
            Paragraph(
                f"""
                <b>Executive Recommendations</b>
                <br/><br/>
                {recommendation_text}
                """,
                bodyStyle
            )
        )

        elements.append(
            Spacer(1,20)
        )


        elements.append(
            Paragraph(
                "Executive Scorecard",
                sectionStyle
            )
        )

        score_table = Table(
        [
            ["Category","Score"],

            ["Venue",
            "100" if event_data.get("venue") else "0"],

            ["Budget",
            "100" if (
                event_data.get("budget_plan")
                or event_data.get("budgetPlan")
            ) else "0"],

            ["Security",
            "100" if event_data.get("security") else "0"],

            ["Execution Readiness",
            f"{readiness_score}"]
        ],
        colWidths=[250,100]
        )

        score_table.setStyle(TableStyle([
            ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#4F46E5")),
            ("TEXTCOLOR",(0,0),(-1,0),colors.white),
            ("GRID",(0,0),(-1,-1),0.5,colors.HexColor("#D1D5DB"))
        ]))

        score_table.hAlign = "CENTER"

        elements.append(score_table)

        elements.append(
            Spacer(1,5)
        )


        # FOOTER

        planner_name = event_data.get(
            "plannerName",
            "Navya"
        )

        planner_email = event_data.get(
            "plannerEmail",
            "contact@aieventplanner.com"
        )

        planner_role = event_data.get(
            "plannerRole",
            "Event Planner"
        )

        footer_table = Table(
            [
                ["Name", planner_name],
                ["Role", planner_role],
                ["Email", planner_email]
            ],
            colWidths=[170, 250]
        )

        elements.append(
            Paragraph(
                "Event Planner Information",
                sectionStyle
            )
        )

        elements.append(
            Spacer(1,10)
        )

        footer_table.setStyle(
            TableStyle([
                ("BACKGROUND",(0,0),(0,-1),colors.HexColor("#F3F4F6")),
                ("FONTNAME",(0,0),(0,-1),"Helvetica-Bold"),
                ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),
                ("GRID",(0,0),(-1,-1),1,colors.grey),
                ("BACKGROUND",(0,1),(0,-1),colors.HexColor("#F3F4F6")),
                ("FONTNAME",(0,1),(0,-1),"Helvetica-Bold"),
                ("BOTTOMPADDING",(0,0),(-1,0),12),
                ("TOPPADDING",(0,0),(-1,0),12)
            ])
            
        )

        footer_table.hAlign = "CENTER"

        elements.append(
            Spacer(1,5)
        )

        elements.append(
            footer_table
        )

        elements.append(
            Paragraph(
                "<hr width='100%'/>",
                styles["BodyText"]
            )
        )

        elements.append(
            Spacer(1,10)
        )

        # =========================
        # BUILD PDF
        # =========================

        print("BUILDING PDF")

        try:

            print("=" * 50)
            print("STARTING PDF BUILD")
            print("=" * 50)

            doc.build(
                elements,
                onFirstPage=add_page_number,
                onLaterPages=add_page_number
            )

            print("=" * 50)
            print("PDF BUILD SUCCESS")
            print("=" * 50)

        except Exception as e:

            print("=" * 50)
            print("PDF BUILD FAILED")
            print(str(e))
            print("=" * 50)

            raise e

        print("PDF BUILD COMPLETE")
