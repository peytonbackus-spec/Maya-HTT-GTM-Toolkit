with monthly_arr as (
    select
        date_trunc('month', close_date) as metric_month,
        sum(amount) as new_arr_added
    from {{ ref('stg_salesforce_opportunities') }}
    where is_won = true
    group by 1
),
monthly_spend as (
    select
        metric_month,
        fully_loaded_gtm_spend
    from {{ ref('stg_financial_opex') }}
)
select
    s.metric_month,
    s.fully_loaded_gtm_spend,
    a.new_arr_added,
    case 
        when a.new_arr_added > 0 
        then round((s.fully_loaded_gtm_spend / a.new_arr_added) * 12, 1)
        else null 
    end as cac_payback_months,
    case 
        when s.fully_loaded_gtm_spend > 0 
        then round(a.new_arr_added / s.fully_loaded_gtm_spend, 2)
        else null 
    end as magic_number
from monthly_spend s
join monthly_arr a on s.metric_month = a.metric_month
order by 1 desc
