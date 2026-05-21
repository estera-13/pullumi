import pulumi

from components import RegionalBucket

regions = [
    ("us-east-1", 30),
    ("us-west-2", 60),
]

buckets = {}

for region, days in regions:

    bucket = RegionalBucket(
        f"bucket-{region}",
        region=region,
        bucket_name_prefix="mlops",
        lifecycle_days=days
    )

    buckets[region] = bucket.bucket.arn

pulumi.export("bucket_arns", buckets)
