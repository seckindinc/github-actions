{{ config(
    materialized='table',
    unique_key='id'
) }}

SELECT
    id,
    name,
    created_at,
    sum(order_value) total_value  -- missing alias AS and inconsistent spacing
FROM {{ ref('orders') }}
where created_at >= '2024-01-01'
group by id, name, created_at
order by total_value desc
