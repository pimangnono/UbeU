"""
PDF Export: Generate candidate assessment reports as PDF.

Uses reportlab for PDF generation if available,
otherwise falls back to HTML-based export.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Optional

from server.models import CandidateReport


def generate_pdf_report(report: CandidateReport, output_path: str) -> str:
    """
    Generate a PDF report for a candidate.

    Args:
        report: CandidateReport with full assessment data
        output_path: Path to save the PDF

    Returns:
        Path to the generated PDF
    """
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.units import inch, cm
        from reportlab.lib.colors import HexColor
        from reportlab.platypus import (
            SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
            PageBreak, Image
        )
        from reportlab.lib import colors

        return _generate_reportlab_pdf(report, output_path)

    except ImportError:
        # Fallback to HTML
        html_path = output_path.replace(".pdf", ".html")
        return _generate_html_report(report, html_path)


def _generate_reportlab_pdf(report: CandidateReport, output_path: str) -> str:
    """Generate PDF using reportlab."""
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch, cm
    from reportlab.lib.colors import HexColor
    from reportlab.platypus import (
        SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
    )
    from reportlab.lib import colors

    doc = SimpleDocTemplate(output_path, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    # Title
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=20,
    )
    story.append(Paragraph("Candidate Assessment Report", title_style))

    # Header info
    story.append(Paragraph(f"<b>Candidate:</b> {report.name}", styles['Normal']))
    story.append(Paragraph(f"<b>ID:</b> {report.participant_id}", styles['Normal']))
    story.append(Paragraph(f"<b>Date:</b> {report.assessment_date.strftime('%Y-%m-%d')}", styles['Normal']))
    story.append(Spacer(1, 0.5 * inch))

    # Mode 1: Logical Assessment
    if report.logic_assessment:
        story.append(Paragraph("Mode 1: Case Study Assessment", styles['Heading2']))

        logic_data = [
            ['Dimension', 'Score', 'Rating'],
        ]

        dimensions = [
            ('problem_structuring', 'Problem Structuring'),
            ('hypothesis_thinking', 'Hypothesis Thinking'),
            ('quantitative_reasoning', 'Quantitative Reasoning'),
            ('data_synthesis', 'Data Synthesis'),
            ('recommendation_quality', 'Recommendation Quality'),
            ('communication_clarity', 'Communication Clarity'),
        ]

        assessment = report.logic_assessment
        if isinstance(assessment, dict):
            for key, label in dimensions:
                dim_data = assessment.get(key, {})
                if isinstance(dim_data, dict):
                    score = dim_data.get('score', 0)
                    rating = _score_to_rating(score)
                    logic_data.append([label, f"{score}/5", rating])

        if len(logic_data) > 1:
            table = Table(logic_data, colWidths=[3*inch, 1*inch, 1.5*inch])
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1E3A5F')),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 12),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#F5F7FA')),
                ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#CCCCCC')),
            ]))
            story.append(table)

        story.append(Spacer(1, 0.3 * inch))

    # Mode 2: Personality Assessment
    if report.personality_assessment:
        story.append(Paragraph("Mode 2: Personality Assessment", styles['Heading2']))

        personality_data = [
            ['Trait', 'Score', 'Level'],
        ]

        traits = [
            ('openness', 'Openness'),
            ('conscientiousness', 'Conscientiousness'),
            ('extraversion', 'Extraversion'),
            ('agreeableness', 'Agreeableness'),
            ('neuroticism', 'Neuroticism'),
        ]

        assessment = report.personality_assessment
        if isinstance(assessment, dict):
            for key, label in traits:
                trait_data = assessment.get(key, {})
                if isinstance(trait_data, dict):
                    score = trait_data.get('score', 0.5)
                    level = _trait_level(score)
                    personality_data.append([label, f"{score:.2f}", level])

        if len(personality_data) > 1:
            table = Table(personality_data, colWidths=[2.5*inch, 1*inch, 2*inch])
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1E3A5F')),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 12),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#F5F7FA')),
                ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#CCCCCC')),
            ]))
            story.append(table)

        story.append(Spacer(1, 0.3 * inch))

    # Ground Truth Comparison
    if report.personality_accuracy:
        story.append(Paragraph("Personality Inference Accuracy", styles['Heading2']))

        accuracy_data = [['Trait', 'Ground Truth', 'Inferred', 'Difference']]
        acc = report.personality_accuracy

        for trait in ['O', 'C', 'E', 'A', 'N']:
            trait_acc = acc.get(trait, {})
            if isinstance(trait_acc, dict):
                gt = trait_acc.get('ground_truth', 0)
                inf = trait_acc.get('inferred', 0)
                diff = trait_acc.get('diff', 0)
                accuracy_data.append([
                    trait,
                    f"{gt:.2f}",
                    f"{inf:.2f}",
                    f"{diff:.2f}",
                ])

        if len(accuracy_data) > 1:
            table = Table(accuracy_data, colWidths=[1.5*inch, 1.5*inch, 1.5*inch, 1.5*inch])
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1E3A5F')),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#CCCCCC')),
            ]))
            story.append(table)

    # Footer
    story.append(Spacer(1, 0.5 * inch))
    story.append(Paragraph(
        f"<i>Generated by UbeU V3 on {datetime.now().strftime('%Y-%m-%d %H:%M')}</i>",
        styles['Normal']
    ))

    doc.build(story)
    return output_path


def _generate_html_report(report: CandidateReport, output_path: str) -> str:
    """Generate HTML report as fallback."""
    html = f"""<!DOCTYPE html>
<html>
<head>
    <title>Assessment Report - {report.name}</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; }}
        h1 {{ color: #1E3A5F; }}
        h2 {{ color: #2E5A8F; border-bottom: 2px solid #2E5A8F; padding-bottom: 5px; }}
        table {{ border-collapse: collapse; width: 100%; margin: 20px 0; }}
        th, td {{ border: 1px solid #ddd; padding: 10px; text-align: center; }}
        th {{ background-color: #1E3A5F; color: white; }}
        tr:nth-child(even) {{ background-color: #f5f5f5; }}
        .meta {{ color: #666; margin-bottom: 20px; }}
        .footer {{ margin-top: 40px; color: #999; font-style: italic; }}
    </style>
</head>
<body>
    <h1>Candidate Assessment Report</h1>
    <div class="meta">
        <p><b>Candidate:</b> {report.name}</p>
        <p><b>ID:</b> {report.participant_id}</p>
        <p><b>Date:</b> {report.assessment_date.strftime('%Y-%m-%d')}</p>
    </div>
"""

    # Mode 1
    if report.logic_assessment:
        html += "<h2>Mode 1: Case Study Assessment</h2>\n"
        html += "<table><tr><th>Dimension</th><th>Score</th><th>Rating</th></tr>\n"

        dimensions = [
            ('problem_structuring', 'Problem Structuring'),
            ('hypothesis_thinking', 'Hypothesis Thinking'),
            ('quantitative_reasoning', 'Quantitative Reasoning'),
            ('data_synthesis', 'Data Synthesis'),
            ('recommendation_quality', 'Recommendation Quality'),
            ('communication_clarity', 'Communication Clarity'),
        ]

        assessment = report.logic_assessment
        if isinstance(assessment, dict):
            for key, label in dimensions:
                dim_data = assessment.get(key, {})
                if isinstance(dim_data, dict):
                    score = dim_data.get('score', 0)
                    rating = _score_to_rating(score)
                    html += f"<tr><td>{label}</td><td>{score}/5</td><td>{rating}</td></tr>\n"

        html += "</table>\n"

    # Mode 2
    if report.personality_assessment:
        html += "<h2>Mode 2: Personality Assessment</h2>\n"
        html += "<table><tr><th>Trait</th><th>Score</th><th>Level</th></tr>\n"

        traits = [
            ('openness', 'Openness'),
            ('conscientiousness', 'Conscientiousness'),
            ('extraversion', 'Extraversion'),
            ('agreeableness', 'Agreeableness'),
            ('neuroticism', 'Neuroticism'),
        ]

        assessment = report.personality_assessment
        if isinstance(assessment, dict):
            for key, label in traits:
                trait_data = assessment.get(key, {})
                if isinstance(trait_data, dict):
                    score = trait_data.get('score', 0.5)
                    level = _trait_level(score)
                    html += f"<tr><td>{label}</td><td>{score:.2f}</td><td>{level}</td></tr>\n"

        html += "</table>\n"

    html += f"""
    <div class="footer">
        Generated by UbeU V3 on {datetime.now().strftime('%Y-%m-%d %H:%M')}
    </div>
</body>
</html>
"""

    with open(output_path, 'w') as f:
        f.write(html)

    return output_path


def _score_to_rating(score: int) -> str:
    """Convert 1-5 score to rating label."""
    ratings = {
        1: "Needs Development",
        2: "Below Expectations",
        3: "Meets Expectations",
        4: "Exceeds Expectations",
        5: "Exceptional",
    }
    return ratings.get(score, "N/A")


def _trait_level(score: float) -> str:
    """Convert 0-1 trait score to level description."""
    if score < 0.3:
        return "Low"
    elif score < 0.5:
        return "Moderately Low"
    elif score < 0.7:
        return "Moderate"
    elif score < 0.85:
        return "Moderately High"
    else:
        return "High"


# API endpoint helper
def export_candidate_pdf(participant_id: str, data_dir: str = "outputs/participants") -> str:
    """Export a candidate's report as PDF."""
    from server.participant_manager import ParticipantManager

    mgr = ParticipantManager(base_dir=data_dir)
    record = mgr.get_participant(participant_id)

    if not record:
        raise ValueError(f"Participant {participant_id} not found")

    report = CandidateReport(
        participant_id=record.participant_id,
        name=record.name,
        assessment_date=record.completed_at or record.created_at,
        bfi44_scores=record.bfi44_scores,
        logic_assessment=record.case_assessment,
        case_stats=record.case_stats,
        personality_assessment=record.group_assessment,
        group_stats=record.group_stats,
        survey=record.survey,
    )

    output_dir = Path(data_dir) / participant_id
    output_path = str(output_dir / f"{participant_id}_report.pdf")

    return generate_pdf_report(report, output_path)
