"""
V3 UI Pages: Full page implementations for dual-mode interview platform.
"""

from ui.pages.consent_page import show_consent_page
from ui.pages.bfi44_page import show_bfi44_page
from ui.pages.case_interview_page import show_case_interview_page
from ui.pages.group_discussion_page import show_group_discussion_page
from ui.pages.results_page import show_results_page
from ui.pages.survey_page import show_survey_page
from ui.pages.admin_dashboard import show_admin_dashboard

__all__ = [
    "show_consent_page",
    "show_bfi44_page",
    "show_case_interview_page",
    "show_group_discussion_page",
    "show_results_page",
    "show_survey_page",
    "show_admin_dashboard",
]
