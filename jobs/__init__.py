from dagster import define_asset_job, AssetSelection
from ..partitions import monthly_partition, weekly_partition

trips_by_week = AssetSelection.keys(["trips_by_week"])
adhoc_request = AssetSelection.keys(["adhoc_request"])

#only calculate trip by week statistics
weekly_update_job = define_asset_job(
  name="weekly_update_job",
  partitions_def=weekly_partition,
  selection=trips_by_week,
)

#all steps except weekly trip stats
trip_update_job = define_asset_job(
    name="trip_update_job",
    partitions_def=monthly_partition,
    selection=AssetSelection.all() - trips_by_week - adhoc_request
)

adhoc_request_job = define_asset_job(
  name="adhoc_request_job",
  selection=adhoc_request,
)

