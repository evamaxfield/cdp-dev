#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from pathlib import Path

import git
from cdp_backend.pipeline import ingestion_models
from gcsfs import GCSFileSystem

###############################################################################

GITHUB_URI = "https://github.com/CouncilDataProject/cdp-backend/commit"

###############################################################################

# Get commit SHA of cdp-backend for event details storage
REPO = git.Repo(Path(__file__).parent.parent.parent / "cdp-backend")
COMMIT = REPO.head.object.hexsha

###############################################################################

# Download raw video again because prior pipeline run likely deleted the file
fs = GCSFileSystem(project="cdp-king-county-b656c71b", token="anon")
fs.get(
    "gs://cdp-king-county-b656c71b.appspot.com/05b39ab44133d3c9f4e24470ec44494b49ec48f18794ed9b461d31c3fa278f90-video.mp4",
    "raw.mp4",
)

# Construct the event
e = ingestion_models.EventIngestionModel(
    body=ingestion_models.Body("Speech Recognition Config Tests"),
    sessions=[
        ingestion_models.Session(
            session_datetime=datetime.now(),
            video_uri=str(Path("raw.mp4").resolve()),
            session_index=0,
        ),
    ],
    event_minutes_items=[
        ingestion_models.EventMinutesItem(
            minutes_item=ingestion_models.MinutesItem(
                name=f"Commit {COMMIT}",
                description=f"{GITHUB_URI}/{COMMIT}",
            )
        ),
    ],
)

# Save event details out
details_file = f"{COMMIT}.json"
with open(details_file, "w") as open_f:
    open_f.write(e.to_json())

# Print out the command to run
print(
    f"Run the following: "
    f"process_special_event "
    f"--event_details_file {details_file} "
    f"--event_gather_config_file pipeline-config.json"
)
