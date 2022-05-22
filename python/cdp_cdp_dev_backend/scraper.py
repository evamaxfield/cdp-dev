#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from typing import List

from cdp_backend.pipeline import ingestion_models

###############################################################################


def get_events(
    from_dt: datetime,
    to_dt: datetime,
    **kwargs,
) -> List[ingestion_models.EventIngestionModel]:
    """
    Get all events for the provided timespan.

    Parameters
    ----------
    from_dt: datetime
        Datetime to start event gather from.
    to_dt: datetime
        Datetime to end event gather at.

    Returns
    -------
    events: List[EventIngestionModel]
        All events gathered that occured in the provided time range.

    Notes
    -----
    As the implimenter of the get_events function, you can choose to ignore the from_dt
    and to_dt parameters. However, they are useful for manually kicking off pipelines
    from GitHub Actions UI.
    """

    event = ingestion_models.EventIngestionModel(
        body=ingestion_models.Body(name="Example Oakland Events", is_active=True),
        sessions=[
            ingestion_models.Session(
                session_datetime=datetime.now(),
                video_uri=(
                    "https://archive-stream.granicus.com/OnDemand/_definst_/mp4:oakland/"
                    "oakland_fa356edd-b6a3-4532-8118-3ce4881783f4.mp4/playlist.m3u8"
                ),
                session_index=0,
            )
        ],
    )
    return [event]
