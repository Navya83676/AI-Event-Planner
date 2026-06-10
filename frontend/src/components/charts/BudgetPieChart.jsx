import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  ResponsiveContainer,
  Legend
} from "recharts";

import {
  useContext
} from "react";

import {
  EventContext
} from "../../context/EventContext";

const COLOR_MAP = {
  venue_cost: "#3b82f6",
  food_cost: "#22c55e",
  decoration_cost: "#f97316",
  security_cost: "#8b5cf6",
  miscellaneous_cost: "#ec4899",
  reserve_cost: "#14b8a6"
};

function BudgetPieChart() {

  const {
    eventData
  } = useContext(EventContext);

  const budgetPlan =
    eventData?.budgetPlan ||
    eventData?.workflowData?.budgetPlan ||
    
    {};

  const data = Object.entries(budgetPlan)
.filter(
 ([key, value]) =>

 ![
   "tool_recommendation",
   "error",
   "remaining_budget",
   "total_estimated_cost",
   "reserve_cost"
 ].includes(key)

 && Number(value) > 0
)
.map(([key, value]) => ({

 key,

 name: key
   .replaceAll("_", " ")
   .replace(/\b\w/g, c => c.toUpperCase()),

 value: Number(value)

}));

console.log(
  "PIE DATA",
  data
);

  return (

    <div
      style={{
        width: "100%",
        height: "320px"
      }}
    >

      <ResponsiveContainer width="100%" height="100%">

        <PieChart>

          <Pie
            data={data}
            innerRadius={70}
            outerRadius={110}
            paddingAngle={4}
             dataKey="value"
          >
               {data.map((entry, index) => (
                  <Cell
                    key={index}
                    fill={COLOR_MAP[entry.key] ||
                       "#94a3b8"

                    }
                  />
                ))}
              </Pie>

              <Tooltip />

              </PieChart>

      </ResponsiveContainer>

    </div>
  );
}

export default BudgetPieChart;