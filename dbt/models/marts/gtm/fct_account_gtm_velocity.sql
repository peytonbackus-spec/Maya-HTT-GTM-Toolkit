with stage_history as (
    select
        opportunity_id,
        account_id,
        stage_name,
        created_at,
        lag(created_at) over (partition by opportunity_id order by created_at) as prev_stage_at
    from {{ ref('stg_salesforce_opportunity_history') }}
),
velocity_calc as (
    select
        opportunity_id,
        account_id,
        stage_name,
        datediff('day', prev_stage_at, created_at) as days_in_stage
    from stage_history
    where prev_stage_at is not null
)
select
    account_id,
    avg(days_in_stage) as avg_stage_duration_days,
    count(distinct opportunity_id) as total_opps
from velocity_calc
group by 1
