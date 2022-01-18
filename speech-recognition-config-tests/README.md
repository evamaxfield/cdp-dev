# Speech Recognition Config Tests

This directory hosts the event gather processing config files for tests I am running
on variations of Google Speech-to-Text processing options.

I have stripped out the actual minutes items and am overloading those as a way to keep
note of which options I am testing for that processing run.

The original King County event used for these tests is:
[http://councildataproject.org/king-county/#/events/e43951e73b40](http://councildataproject.org/king-county/#/events/e43951e73b40)

## Running Tests

After making changes to the
[Google Speech-to-Text SR Model](https://github.com/CouncilDataProject/cdp-backend/blob/feature/improved-gsr/cdp_backend/sr_models/google_cloud_sr_model.py),
commit your changes, push your changes to the
[`feature/improved-gsr` branch](https://github.com/CouncilDataProject/cdp-backend/tree/feature/improved-gsr),
then run the `make-test-event-details.py` file.

```bash
python make-test-event-details.py
```

Once the test config has been created, run the command that should have printed out.
For example:

```bash
process_special_event --event_details_file abcd1234.json --event_gather_config_file pipeline_config.json
```

## Tests

metadata interaction type: DISCUSSION vs PHONE_CALL
speech adaption: none vs some
model: default vs video

-   Baseline (v3.0.2):

    -   Config:
        -   Metadata Interaction Type: discussion
        -   Speech Adaption: none
        -   Model: default
    -   [Event Details JSON](./23124d870b95ef3bb2d7f770d230ca383b57b09c.json)
    -   [Event Page](https://jacksonmaxfield.github.io/cdp-dev/#/events/1126b685f94d)

-   Whole Suite Upgrades:

    -   Config:
        -   Metadata Interaction Type: phone_call
        -   Speech Adaption: added
        -   Model: video
    -   [Event Details JSON](./71f8ae4404f426ff98e36860e83fa9dde367d0d5.json)
    -   [Event Page](https://jacksonmaxfield.github.io/cdp-dev/#/events/6f15f3db0b19)

-   Upgrade, Remove Alphanumeric Sequences Adaption:

    -   Config:
        -   Metadata Interaction Type: phone_call
        -   Speech Adaption: added
        -   Model: video
    -   [Event Details JSON](./e97008614132e7f20f764d8e6b7d121e5f60889f.json)
    -   [Event Page](https://jacksonmaxfield.github.io/cdp-dev/#/events/38fa2d6e0603)

-   Upgrade, Replace $YEAR and $POSTCODE with Numeric Seq:

    -   Config:
        -   Metadata Interaction Type: phone_call
        -   Speech Adaption: added
        -   Model: video
    -   [Event Details JSON](./3a39e0c70e2d5e506cc1238c87b56a278ee36b63.json)
    -   [Event Page](https://jacksonmaxfield.github.io/cdp-dev/#/events/7d4212911c66)
