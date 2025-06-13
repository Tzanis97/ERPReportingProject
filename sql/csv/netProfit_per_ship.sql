SELECT 
    s.name AS ShipName,
    SUM(v.total_revenue_usd) AS TotalRevenue,
    SUM(v.fuel_cost_usd) AS TotalFuelCost,
    SUM(v.operational_cost_usd) AS TotalOperationalCost,
    SUM(v.total_revenue_usd) 
        - SUM(v.fuel_cost_usd) 
        - SUM(v.operational_cost_usd) AS NetProfit
FROM 'data/voyages_with_kpis.csv' v 
JOIN 'data/ships.csv' s
    ON v.ship_id = s.ship_id
GROUP BY s.name
ORDER BY NetProfit DESC;