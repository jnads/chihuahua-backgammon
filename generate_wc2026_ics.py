#!/usr/bin/env python3
"""
generate_wc2026_ics.py
Generates world_cup_2026.ics with all 104 FIFA World Cup 2026 matches.

Times are stored as UTC; Google Calendar displays them in your local timezone.
Each event description also shows the Portugal kickoff time (WEST = UTC+1).

Import into Google Calendar:
  Settings (⚙️) → Import & export → Select file → choose "Free time" calendar → Import
"""

from datetime import datetime, timedelta
import pytz
from icalendar import Calendar, Event, vText

ET_TZ    = pytz.timezone("America/New_York")   # EDT = UTC-4 in summer
LISBON   = pytz.timezone("Europe/Lisbon")       # WEST = UTC+1 in summer

# ---------------------------------------------------------------------------
# ALL 104 MATCHES
# Times in Eastern Time (EDT = UTC-4). Source: NBC Sports official schedule.
# ---------------------------------------------------------------------------
MATCHES = [

    # ── GROUP STAGE ─────────────────────────────────────────────────────────

    # Group A
    {"num": 1,  "round": "Group A", "a": "Mexico",               "b": "South Africa",           "date": "2026-06-11", "time": "15:00", "stadium": "Estadio Azteca",          "city": "Mexico City",     "country": "Mexico"},
    {"num": 2,  "round": "Group A", "a": "South Korea",          "b": "Czechia",                "date": "2026-06-11", "time": "22:00", "stadium": "Estadio Akron",           "city": "Guadalajara",     "country": "Mexico"},
    {"num": 3,  "round": "Group A", "a": "Czechia",              "b": "South Africa",           "date": "2026-06-18", "time": "12:00", "stadium": "Mercedes-Benz Stadium",   "city": "Atlanta",         "country": "USA"},
    {"num": 4,  "round": "Group A", "a": "Mexico",               "b": "South Korea",            "date": "2026-06-18", "time": "21:00", "stadium": "Estadio Akron",           "city": "Guadalajara",     "country": "Mexico"},
    {"num": 5,  "round": "Group A", "a": "Czechia",              "b": "Mexico",                 "date": "2026-06-24", "time": "21:00", "stadium": "Estadio Azteca",          "city": "Mexico City",     "country": "Mexico"},
    {"num": 6,  "round": "Group A", "a": "South Africa",         "b": "South Korea",            "date": "2026-06-24", "time": "21:00", "stadium": "Estadio BBVA",            "city": "Monterrey",       "country": "Mexico"},

    # Group B
    {"num": 7,  "round": "Group B", "a": "Canada",               "b": "Bosnia & Herzegovina",   "date": "2026-06-12", "time": "15:00", "stadium": "BMO Field",               "city": "Toronto",         "country": "Canada"},
    {"num": 8,  "round": "Group B", "a": "Qatar",                "b": "Switzerland",            "date": "2026-06-13", "time": "15:00", "stadium": "Levi's Stadium",          "city": "Santa Clara",     "country": "USA"},
    {"num": 9,  "round": "Group B", "a": "Switzerland",          "b": "Bosnia & Herzegovina",   "date": "2026-06-18", "time": "15:00", "stadium": "SoFi Stadium",            "city": "Inglewood",       "country": "USA"},
    {"num": 10, "round": "Group B", "a": "Canada",               "b": "Qatar",                  "date": "2026-06-18", "time": "18:00", "stadium": "BC Place",                 "city": "Vancouver",       "country": "Canada"},
    {"num": 11, "round": "Group B", "a": "Switzerland",          "b": "Canada",                 "date": "2026-06-24", "time": "15:00", "stadium": "BC Place",                 "city": "Vancouver",       "country": "Canada"},
    {"num": 12, "round": "Group B", "a": "Bosnia & Herzegovina", "b": "Qatar",                  "date": "2026-06-24", "time": "15:00", "stadium": "Lumen Field",             "city": "Seattle",         "country": "USA"},

    # Group C
    {"num": 13, "round": "Group C", "a": "Brazil",               "b": "Morocco",                "date": "2026-06-13", "time": "18:00", "stadium": "MetLife Stadium",         "city": "East Rutherford", "country": "USA"},
    {"num": 14, "round": "Group C", "a": "Haiti",                "b": "Scotland",               "date": "2026-06-13", "time": "21:00", "stadium": "Gillette Stadium",        "city": "Foxborough",      "country": "USA"},
    {"num": 15, "round": "Group C", "a": "Scotland",             "b": "Morocco",                "date": "2026-06-19", "time": "18:00", "stadium": "Gillette Stadium",        "city": "Foxborough",      "country": "USA"},
    {"num": 16, "round": "Group C", "a": "Brazil",               "b": "Haiti",                  "date": "2026-06-19", "time": "21:00", "stadium": "Lincoln Financial Field", "city": "Philadelphia",    "country": "USA"},
    {"num": 17, "round": "Group C", "a": "Scotland",             "b": "Brazil",                 "date": "2026-06-24", "time": "18:00", "stadium": "Hard Rock Stadium",       "city": "Miami Gardens",   "country": "USA"},
    {"num": 18, "round": "Group C", "a": "Morocco",              "b": "Haiti",                  "date": "2026-06-24", "time": "18:00", "stadium": "Mercedes-Benz Stadium",   "city": "Atlanta",         "country": "USA"},

    # Group D
    {"num": 19, "round": "Group D", "a": "USA",                  "b": "Paraguay",               "date": "2026-06-12", "time": "21:00", "stadium": "SoFi Stadium",            "city": "Inglewood",       "country": "USA"},
    {"num": 20, "round": "Group D", "a": "Australia",            "b": "Turkiye",                "date": "2026-06-13", "time": "00:00", "stadium": "BC Place",                 "city": "Vancouver",       "country": "Canada"},
    {"num": 21, "round": "Group D", "a": "USA",                  "b": "Australia",              "date": "2026-06-19", "time": "15:00", "stadium": "Lumen Field",             "city": "Seattle",         "country": "USA"},
    {"num": 22, "round": "Group D", "a": "Turkiye",              "b": "Paraguay",               "date": "2026-06-20", "time": "00:00", "stadium": "Levi's Stadium",          "city": "Santa Clara",     "country": "USA"},
    {"num": 23, "round": "Group D", "a": "Turkiye",              "b": "USA",                    "date": "2026-06-25", "time": "22:00", "stadium": "SoFi Stadium",            "city": "Inglewood",       "country": "USA"},
    {"num": 24, "round": "Group D", "a": "Paraguay",             "b": "Australia",              "date": "2026-06-25", "time": "22:00", "stadium": "Levi's Stadium",          "city": "Santa Clara",     "country": "USA"},

    # Group E
    {"num": 25, "round": "Group E", "a": "Germany",              "b": "Curacao",                "date": "2026-06-14", "time": "13:00", "stadium": "NRG Stadium",             "city": "Houston",         "country": "USA"},
    {"num": 26, "round": "Group E", "a": "Ivory Coast",          "b": "Ecuador",                "date": "2026-06-14", "time": "19:00", "stadium": "Lincoln Financial Field", "city": "Philadelphia",    "country": "USA"},
    {"num": 27, "round": "Group E", "a": "Germany",              "b": "Ivory Coast",            "date": "2026-06-20", "time": "16:00", "stadium": "BMO Field",               "city": "Toronto",         "country": "Canada"},
    {"num": 28, "round": "Group E", "a": "Ecuador",              "b": "Curacao",                "date": "2026-06-20", "time": "20:00", "stadium": "Arrowhead Stadium",       "city": "Kansas City",     "country": "USA"},
    {"num": 29, "round": "Group E", "a": "Ecuador",              "b": "Germany",                "date": "2026-06-25", "time": "16:00", "stadium": "MetLife Stadium",         "city": "East Rutherford", "country": "USA"},
    {"num": 30, "round": "Group E", "a": "Curacao",              "b": "Ivory Coast",            "date": "2026-06-25", "time": "16:00", "stadium": "Lincoln Financial Field", "city": "Philadelphia",    "country": "USA"},

    # Group F
    {"num": 31, "round": "Group F", "a": "Netherlands",          "b": "Japan",                  "date": "2026-06-14", "time": "16:00", "stadium": "AT&T Stadium",            "city": "Arlington",       "country": "USA"},
    {"num": 32, "round": "Group F", "a": "Sweden",               "b": "Tunisia",                "date": "2026-06-14", "time": "22:00", "stadium": "Estadio BBVA",            "city": "Monterrey",       "country": "Mexico"},
    {"num": 33, "round": "Group F", "a": "Netherlands",          "b": "Sweden",                 "date": "2026-06-20", "time": "13:00", "stadium": "NRG Stadium",             "city": "Houston",         "country": "USA"},
    {"num": 34, "round": "Group F", "a": "Tunisia",              "b": "Japan",                  "date": "2026-06-21", "time": "00:00", "stadium": "Estadio BBVA",            "city": "Monterrey",       "country": "Mexico"},
    {"num": 35, "round": "Group F", "a": "Japan",                "b": "Sweden",                 "date": "2026-06-25", "time": "19:00", "stadium": "AT&T Stadium",            "city": "Arlington",       "country": "USA"},
    {"num": 36, "round": "Group F", "a": "Tunisia",              "b": "Netherlands",            "date": "2026-06-25", "time": "19:00", "stadium": "Arrowhead Stadium",       "city": "Kansas City",     "country": "USA"},

    # Group G
    {"num": 37, "round": "Group G", "a": "Iran",                 "b": "New Zealand",            "date": "2026-06-15", "time": "21:00", "stadium": "SoFi Stadium",            "city": "Inglewood",       "country": "USA"},
    {"num": 38, "round": "Group G", "a": "Belgium",              "b": "Egypt",                  "date": "2026-06-15", "time": "15:00", "stadium": "Lumen Field",             "city": "Seattle",         "country": "USA"},
    {"num": 39, "round": "Group G", "a": "Belgium",              "b": "Iran",                   "date": "2026-06-21", "time": "15:00", "stadium": "SoFi Stadium",            "city": "Inglewood",       "country": "USA"},
    {"num": 40, "round": "Group G", "a": "New Zealand",          "b": "Egypt",                  "date": "2026-06-21", "time": "21:00", "stadium": "BC Place",                 "city": "Vancouver",       "country": "Canada"},
    {"num": 41, "round": "Group G", "a": "Egypt",                "b": "Iran",                   "date": "2026-06-26", "time": "23:00", "stadium": "Lumen Field",             "city": "Seattle",         "country": "USA"},
    {"num": 42, "round": "Group G", "a": "New Zealand",          "b": "Belgium",                "date": "2026-06-26", "time": "23:00", "stadium": "BC Place",                 "city": "Vancouver",       "country": "Canada"},

    # Group H
    {"num": 43, "round": "Group H", "a": "Spain",                "b": "Cape Verde",             "date": "2026-06-15", "time": "12:00", "stadium": "Mercedes-Benz Stadium",   "city": "Atlanta",         "country": "USA"},
    {"num": 44, "round": "Group H", "a": "Saudi Arabia",         "b": "Uruguay",                "date": "2026-06-15", "time": "18:00", "stadium": "Hard Rock Stadium",       "city": "Miami Gardens",   "country": "USA"},
    {"num": 45, "round": "Group H", "a": "Spain",                "b": "Saudi Arabia",           "date": "2026-06-21", "time": "12:00", "stadium": "Mercedes-Benz Stadium",   "city": "Atlanta",         "country": "USA"},
    {"num": 46, "round": "Group H", "a": "Uruguay",              "b": "Cape Verde",             "date": "2026-06-21", "time": "18:00", "stadium": "Hard Rock Stadium",       "city": "Miami Gardens",   "country": "USA"},
    {"num": 47, "round": "Group H", "a": "Cape Verde",           "b": "Saudi Arabia",           "date": "2026-06-26", "time": "20:00", "stadium": "NRG Stadium",             "city": "Houston",         "country": "USA"},
    {"num": 48, "round": "Group H", "a": "Uruguay",              "b": "Spain",                  "date": "2026-06-26", "time": "20:00", "stadium": "Estadio Akron",           "city": "Guadalajara",     "country": "Mexico"},

    # Group I
    {"num": 49, "round": "Group I", "a": "France",               "b": "Senegal",                "date": "2026-06-16", "time": "15:00", "stadium": "MetLife Stadium",         "city": "East Rutherford", "country": "USA"},
    {"num": 50, "round": "Group I", "a": "Iraq",                 "b": "Norway",                 "date": "2026-06-16", "time": "18:00", "stadium": "Gillette Stadium",        "city": "Foxborough",      "country": "USA"},
    {"num": 51, "round": "Group I", "a": "France",               "b": "Iraq",                   "date": "2026-06-22", "time": "17:00", "stadium": "Lincoln Financial Field", "city": "Philadelphia",    "country": "USA"},
    {"num": 52, "round": "Group I", "a": "Norway",               "b": "Senegal",                "date": "2026-06-22", "time": "20:00", "stadium": "MetLife Stadium",         "city": "East Rutherford", "country": "USA"},
    {"num": 53, "round": "Group I", "a": "Norway",               "b": "France",                 "date": "2026-06-26", "time": "15:00", "stadium": "Gillette Stadium",        "city": "Foxborough",      "country": "USA"},
    {"num": 54, "round": "Group I", "a": "Senegal",              "b": "Iraq",                   "date": "2026-06-26", "time": "15:00", "stadium": "BMO Field",               "city": "Toronto",         "country": "Canada"},

    # Group J
    {"num": 55, "round": "Group J", "a": "Argentina",            "b": "Algeria",                "date": "2026-06-16", "time": "21:00", "stadium": "Arrowhead Stadium",       "city": "Kansas City",     "country": "USA"},
    {"num": 56, "round": "Group J", "a": "Austria",              "b": "Jordan",                 "date": "2026-06-17", "time": "00:00", "stadium": "Levi's Stadium",          "city": "Santa Clara",     "country": "USA"},
    {"num": 57, "round": "Group J", "a": "Argentina",            "b": "Austria",                "date": "2026-06-22", "time": "13:00", "stadium": "AT&T Stadium",            "city": "Arlington",       "country": "USA"},
    {"num": 58, "round": "Group J", "a": "Jordan",               "b": "Algeria",                "date": "2026-06-22", "time": "23:00", "stadium": "Levi's Stadium",          "city": "Santa Clara",     "country": "USA"},
    {"num": 59, "round": "Group J", "a": "Algeria",              "b": "Austria",                "date": "2026-06-27", "time": "22:00", "stadium": "Arrowhead Stadium",       "city": "Kansas City",     "country": "USA"},
    {"num": 60, "round": "Group J", "a": "Jordan",               "b": "Argentina",              "date": "2026-06-27", "time": "22:00", "stadium": "AT&T Stadium",            "city": "Arlington",       "country": "USA"},

    # Group K  ⭐ PORTUGAL
    {"num": 61, "round": "Group K", "a": "Portugal",             "b": "DR Congo",               "date": "2026-06-17", "time": "13:00", "stadium": "NRG Stadium",             "city": "Houston",         "country": "USA"},
    {"num": 62, "round": "Group K", "a": "Uzbekistan",           "b": "Colombia",               "date": "2026-06-17", "time": "22:00", "stadium": "Estadio Azteca",          "city": "Mexico City",     "country": "Mexico"},
    {"num": 63, "round": "Group K", "a": "Portugal",             "b": "Uzbekistan",             "date": "2026-06-23", "time": "13:00", "stadium": "NRG Stadium",             "city": "Houston",         "country": "USA"},
    {"num": 64, "round": "Group K", "a": "Colombia",             "b": "DR Congo",               "date": "2026-06-23", "time": "22:00", "stadium": "Estadio Akron",           "city": "Guadalajara",     "country": "Mexico"},
    {"num": 65, "round": "Group K", "a": "Colombia",             "b": "Portugal",               "date": "2026-06-27", "time": "19:30", "stadium": "Hard Rock Stadium",       "city": "Miami Gardens",   "country": "USA"},
    {"num": 66, "round": "Group K", "a": "DR Congo",             "b": "Uzbekistan",             "date": "2026-06-27", "time": "19:30", "stadium": "Mercedes-Benz Stadium",   "city": "Atlanta",         "country": "USA"},

    # Group L
    {"num": 67, "round": "Group L", "a": "England",              "b": "Croatia",                "date": "2026-06-17", "time": "16:00", "stadium": "AT&T Stadium",            "city": "Arlington",       "country": "USA"},
    {"num": 68, "round": "Group L", "a": "Ghana",                "b": "Panama",                 "date": "2026-06-17", "time": "19:00", "stadium": "BMO Field",               "city": "Toronto",         "country": "Canada"},
    {"num": 69, "round": "Group L", "a": "England",              "b": "Ghana",                  "date": "2026-06-23", "time": "16:00", "stadium": "Gillette Stadium",        "city": "Foxborough",      "country": "USA"},
    {"num": 70, "round": "Group L", "a": "Panama",               "b": "Croatia",                "date": "2026-06-23", "time": "19:00", "stadium": "BMO Field",               "city": "Toronto",         "country": "Canada"},
    {"num": 71, "round": "Group L", "a": "Panama",               "b": "England",                "date": "2026-06-27", "time": "17:00", "stadium": "MetLife Stadium",         "city": "East Rutherford", "country": "USA"},
    {"num": 72, "round": "Group L", "a": "Croatia",              "b": "Ghana",                  "date": "2026-06-27", "time": "17:00", "stadium": "Lincoln Financial Field", "city": "Philadelphia",    "country": "USA"},

    # ── ROUND OF 32 ─────────────────────────────────────────────────────────

    {"num": 73,  "round": "Round of 32", "a": "Runner-up Group A",        "b": "Runner-up Group B",        "date": "2026-06-28", "time": "15:00", "stadium": "SoFi Stadium",            "city": "Inglewood",       "country": "USA"},
    {"num": 74,  "round": "Round of 32", "a": "Winner Group C",           "b": "Runner-up Group F",        "date": "2026-06-29", "time": "13:00", "stadium": "NRG Stadium",             "city": "Houston",         "country": "USA"},
    {"num": 75,  "round": "Round of 32", "a": "Winner Group E",           "b": "Best 3rd (A/B/C/D/F)",    "date": "2026-06-29", "time": "16:30", "stadium": "Gillette Stadium",        "city": "Foxborough",      "country": "USA"},
    {"num": 76,  "round": "Round of 32", "a": "Winner Group F",           "b": "Runner-up Group C",        "date": "2026-06-29", "time": "21:00", "stadium": "Estadio BBVA",            "city": "Monterrey",       "country": "Mexico"},
    {"num": 77,  "round": "Round of 32", "a": "Runner-up Group E",        "b": "Runner-up Group I",        "date": "2026-06-30", "time": "13:00", "stadium": "AT&T Stadium",            "city": "Arlington",       "country": "USA"},
    {"num": 78,  "round": "Round of 32", "a": "Winner Group I",           "b": "Best 3rd (C/D/F/G/H)",    "date": "2026-06-30", "time": "17:00", "stadium": "MetLife Stadium",         "city": "East Rutherford", "country": "USA"},
    {"num": 79,  "round": "Round of 32", "a": "Winner Group A",           "b": "Best 3rd (C/E/F/H/I)",    "date": "2026-06-30", "time": "21:00", "stadium": "Estadio Azteca",          "city": "Mexico City",     "country": "Mexico"},
    {"num": 80,  "round": "Round of 32", "a": "Winner Group L",           "b": "Best 3rd (E/H/I/J/K)",    "date": "2026-07-01", "time": "12:00", "stadium": "Mercedes-Benz Stadium",   "city": "Atlanta",         "country": "USA"},
    {"num": 81,  "round": "Round of 32", "a": "Winner Group G",           "b": "Best 3rd (A/E/H/I/J)",    "date": "2026-07-01", "time": "16:00", "stadium": "Lumen Field",             "city": "Seattle",         "country": "USA"},
    {"num": 82,  "round": "Round of 32", "a": "Winner Group D",           "b": "Best 3rd (B/E/F/I/J)",    "date": "2026-07-01", "time": "20:00", "stadium": "Levi's Stadium",          "city": "Santa Clara",     "country": "USA"},
    {"num": 83,  "round": "Round of 32", "a": "Winner Group H",           "b": "Runner-up Group J",        "date": "2026-07-02", "time": "15:00", "stadium": "SoFi Stadium",            "city": "Inglewood",       "country": "USA"},
    {"num": 84,  "round": "Round of 32", "a": "Runner-up Group K",        "b": "Runner-up Group L",        "date": "2026-07-02", "time": "19:00", "stadium": "BMO Field",               "city": "Toronto",         "country": "Canada"},
    {"num": 85,  "round": "Round of 32", "a": "Winner Group B",           "b": "Best 3rd (E/F/G/I/J)",    "date": "2026-07-02", "time": "23:00", "stadium": "BC Place",                 "city": "Vancouver",       "country": "Canada"},
    {"num": 86,  "round": "Round of 32", "a": "Runner-up Group D",        "b": "Runner-up Group G",        "date": "2026-07-03", "time": "14:00", "stadium": "AT&T Stadium",            "city": "Arlington",       "country": "USA"},
    {"num": 87,  "round": "Round of 32", "a": "Winner Group J",           "b": "Runner-up Group H",        "date": "2026-07-03", "time": "18:00", "stadium": "Hard Rock Stadium",       "city": "Miami Gardens",   "country": "USA"},
    {"num": 88,  "round": "Round of 32", "a": "Winner Group K",           "b": "Best 3rd (D/E/I/J/L)",    "date": "2026-07-03", "time": "21:30", "stadium": "Arrowhead Stadium",       "city": "Kansas City",     "country": "USA"},

    # ── ROUND OF 16 ─────────────────────────────────────────────────────────

    {"num": 89,  "round": "Round of 16", "a": "Winner Match 73",          "b": "Winner Match 75",          "date": "2026-07-04", "time": "13:00", "stadium": "NRG Stadium",             "city": "Houston",         "country": "USA"},
    {"num": 90,  "round": "Round of 16", "a": "Winner Match 74",          "b": "Winner Match 77",          "date": "2026-07-04", "time": "17:00", "stadium": "Lincoln Financial Field", "city": "Philadelphia",    "country": "USA"},
    {"num": 91,  "round": "Round of 16", "a": "Winner Match 76",          "b": "Winner Match 78",          "date": "2026-07-05", "time": "16:00", "stadium": "MetLife Stadium",         "city": "East Rutherford", "country": "USA"},
    {"num": 92,  "round": "Round of 16", "a": "Winner Match 79",          "b": "Winner Match 80",          "date": "2026-07-05", "time": "20:00", "stadium": "Estadio Azteca",          "city": "Mexico City",     "country": "Mexico"},
    {"num": 93,  "round": "Round of 16", "a": "Winner Match 83",          "b": "Winner Match 84",          "date": "2026-07-06", "time": "15:00", "stadium": "AT&T Stadium",            "city": "Arlington",       "country": "USA"},
    {"num": 94,  "round": "Round of 16", "a": "Winner Match 81",          "b": "Winner Match 82",          "date": "2026-07-06", "time": "20:00", "stadium": "Lumen Field",             "city": "Seattle",         "country": "USA"},
    {"num": 95,  "round": "Round of 16", "a": "Winner Match 86",          "b": "Winner Match 88",          "date": "2026-07-07", "time": "12:00", "stadium": "Mercedes-Benz Stadium",   "city": "Atlanta",         "country": "USA"},
    {"num": 96,  "round": "Round of 16", "a": "Winner Match 85",          "b": "Winner Match 87",          "date": "2026-07-07", "time": "16:00", "stadium": "BC Place",                 "city": "Vancouver",       "country": "Canada"},

    # ── QUARTER-FINALS ──────────────────────────────────────────────────────

    {"num": 97,  "round": "Quarter-Final", "a": "Winner Match 89",        "b": "Winner Match 90",          "date": "2026-07-09", "time": "16:00", "stadium": "Gillette Stadium",        "city": "Foxborough",      "country": "USA"},
    {"num": 98,  "round": "Quarter-Final", "a": "Winner Match 93",        "b": "Winner Match 94",          "date": "2026-07-10", "time": "15:00", "stadium": "SoFi Stadium",            "city": "Inglewood",       "country": "USA"},
    {"num": 99,  "round": "Quarter-Final", "a": "Winner Match 91",        "b": "Winner Match 92",          "date": "2026-07-11", "time": "17:00", "stadium": "Hard Rock Stadium",       "city": "Miami Gardens",   "country": "USA"},
    {"num": 100, "round": "Quarter-Final", "a": "Winner Match 95",        "b": "Winner Match 96",          "date": "2026-07-11", "time": "21:00", "stadium": "Arrowhead Stadium",       "city": "Kansas City",     "country": "USA"},

    # ── SEMI-FINALS ─────────────────────────────────────────────────────────

    {"num": 101, "round": "Semi-Final",   "a": "Winner Match 97",         "b": "Winner Match 98",          "date": "2026-07-14", "time": "15:00", "stadium": "AT&T Stadium",            "city": "Arlington",       "country": "USA"},
    {"num": 102, "round": "Semi-Final",   "a": "Winner Match 99",         "b": "Winner Match 100",         "date": "2026-07-15", "time": "15:00", "stadium": "Mercedes-Benz Stadium",   "city": "Atlanta",         "country": "USA"},

    # ── THIRD-PLACE & FINAL ─────────────────────────────────────────────────

    {"num": 103, "round": "Third-Place Match", "a": "Loser Match 101",    "b": "Loser Match 102",          "date": "2026-07-18", "time": "17:00", "stadium": "Hard Rock Stadium",       "city": "Miami Gardens",   "country": "USA"},
    {"num": 104, "round": "FINAL",             "a": "Winner Match 101",   "b": "Winner Match 102",         "date": "2026-07-19", "time": "15:00", "stadium": "MetLife Stadium",         "city": "East Rutherford", "country": "USA"},
]

# ---------------------------------------------------------------------------
# TBD keywords — used to detect knockout matches with unknown opponents
# ---------------------------------------------------------------------------
TBD_KEYWORDS = ("Winner", "Runner-up", "Best", "Loser")


def is_tbd(name):
    return any(k in name for k in TBD_KEYWORDS)


def build_title(m):
    """Build calendar event title."""
    if is_tbd(m["a"]) or is_tbd(m["b"]):
        return f"\U0001f3c6 {m['round']} | WC2026"          # 🏆
    return f"\U0001f3c6 {m['a']} vs {m['b']} | WC2026"


def build_description(m, lisbon_dt):
    """Build multi-line event description."""
    lines = [
        f"\u26bd {m['a']} vs {m['b']}",                    # ⚽
        f"\U0001f5d3  Round: {m['round']}",                  # 🗓
        f"\U0001f3df  Venue: {m['stadium']}, {m['city']}, {m['country']}",  # 🏟
        f"\U0001f550 Kick-off Portugal: {lisbon_dt.strftime('%H:%M')} WEST",  # 🕐
        "",
        "\U0001f4fa Watch in Portugal: Sport TV / LiveMode TV",  # 📺
        "",
        f"FIFA World Cup 2026\u2122 | Match #{m['num']}",
    ]
    return "\\n".join(lines)


def build_event(m):
    """Build a single icalendar Event from a match dict."""
    # Parse ET kickoff and convert to UTC and Lisbon
    h, mi = map(int, m["time"].split(":"))
    naive = datetime.strptime(m["date"], "%Y-%m-%d").replace(hour=h, minute=mi)
    et_dt     = ET_TZ.localize(naive)
    utc_dt    = et_dt.astimezone(pytz.utc)
    lisbon_dt = utc_dt.astimezone(LISBON)
    utc_end   = utc_dt + timedelta(hours=2)

    ev = Event()
    ev.add("uid",      f"wc2026-match-{m['num']}@fifaportugal")
    ev.add("dtstamp",  datetime(2026, 4, 1, tzinfo=pytz.utc))   # fixed → idempotent
    ev.add("dtstart",  utc_dt)
    ev.add("dtend",    utc_end)
    ev.add("summary",  build_title(m))
    ev["description"] = vText(build_description(m, lisbon_dt))
    ev.add("location", f"{m['stadium']}, {m['city']}, {m['country']}")
    ev.add("categories", ["SPORTS", "FOOTBALL"])
    return ev


def build_calendar():
    """Assemble all 104 match events into a Calendar object."""
    cal = Calendar()
    cal.add("prodid",  "-//FIFA WC2026 Portugal Calendar//EN")
    cal.add("version", "2.0")
    cal.add("calscale","GREGORIAN")
    cal.add("method",  "PUBLISH")
    # Google Calendar hints
    cal["X-WR-CALNAME"] = "FIFA World Cup 2026"
    cal["X-WR-TIMEZONE"] = "Europe/Lisbon"
    cal["X-WR-CALDESC"] = "All 104 FIFA World Cup 2026 matches with Portugal kick-off times"

    for m in MATCHES:
        cal.add_component(build_event(m))
    return cal


def main():
    print(f"Building calendar for {len(MATCHES)} matches...")
    cal = build_calendar()
    output_path = "world_cup_2026.ics"
    with open(output_path, "wb") as f:
        f.write(cal.to_ical())
    print(f"Done! Created: {output_path}")
    print()
    print("SPOT CHECKS (Portugal time = ET + 5h):")
    checks = [
        (1,  "Mexico vs South Africa — 3pm ET → 20:00 WEST"),
        (61, "Portugal vs DR Congo   — 1pm ET → 18:00 WEST"),
        (63, "Portugal vs Uzbekistan — 1pm ET → 18:00 WEST"),
        (65, "Colombia vs Portugal   — 7:30pm ET → 00:30 WEST (+1 day)"),
        (104,"FINAL                  — 3pm ET → 20:00 WEST"),
    ]
    et_tz = pytz.timezone("America/New_York")
    lisbon = pytz.timezone("Europe/Lisbon")
    for num, label in checks:
        m = next(x for x in MATCHES if x["num"] == num)
        h, mi = map(int, m["time"].split(":"))
        naive = datetime.strptime(m["date"], "%Y-%m-%d").replace(hour=h, minute=mi)
        et_dt = et_tz.localize(naive)
        lisbon_dt = et_dt.astimezone(lisbon)
        print(f"  Match {num:3d}: {label}")
        print(f"           → Portugal: {lisbon_dt.strftime('%A %d %b %Y %H:%M')} WEST")
    print()
    print("HOW TO IMPORT INTO GOOGLE CALENDAR:")
    print("  1. Go to https://calendar.google.com")
    print("  2. Click ⚙️ → Settings → Import & export")
    print("  3. Click 'Select file' → choose world_cup_2026.ics")
    print("  4. Set 'Add to calendar' → Free time")
    print("  5. Click Import → confirm '104 events imported'")


if __name__ == "__main__":
    main()
