import sentry_sdk

sentry_sdk.init(
    dsn="https://2dba7b137b74dd95244522bb99103892@o4511554270396416.ingest.de.sentry.io/4511554513731664",
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
)
division_by_zero = 1 / 0
