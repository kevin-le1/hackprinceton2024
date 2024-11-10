"use client";

import {
  Label,
  PolarGrid,
  PolarRadiusAxis,
  RadialBar,
  RadialBarChart,
} from "recharts";

import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "./ui/card";
import { ChartConfig, ChartContainer } from "./ui/chart";
import api from "../api/api";

const chartConfig = {
  visitors: {
    label: "Visitors",
  },
  safari: {
    label: "Safari",
    color: "hsl(var(--chart-2))",
  },
} satisfies ChartConfig;

export default function Chart() {
  const totalVisitors = 50; // Total visitors for reference

  // GET receives all patient data, including UUID & refetching mechanism
  const { data: patients } = api.endpoints.getPatientAll.useQuery();

  const currentVisitors = patients ? patients.length : 0;
  const proportion = (currentVisitors / totalVisitors) * 100;
  const chartData = [
    {
      browser: "safari",
      visitors: currentVisitors,
      fill: "#E98074",
    },
  ];
  return (
    <Card className="flex flex-col max-h-[350px]">
      <CardHeader className="items-center pb-0">
        <CardTitle>Hospital Load</CardTitle>
        <CardDescription>Current</CardDescription>
      </CardHeader>
      <CardContent className="flex-1 pb-0">
        <ChartContainer
          config={chartConfig}
          className="mx-auto aspect-square max-h-[220px]"
        >
          <RadialBarChart
            data={chartData}
            startAngle={0}
            endAngle={(proportion / 100) * 360}
            innerRadius={80}
            outerRadius={110}
          >
            <PolarGrid
              gridType="circle"
              radialLines={false}
              stroke="none"
              className="first:fill-muted last:fill-text-black"
              polarRadius={[86, 74]}
            />
            <RadialBar dataKey="visitors" background cornerRadius={10} />
            <PolarRadiusAxis tick={false} tickLine={false} axisLine={false}>
              <Label
                content={({ viewBox }) => {
                  if (viewBox && "cx" in viewBox && "cy" in viewBox) {
                    return (
                      <text
                        x={viewBox.cx}
                        y={viewBox.cy}
                        textAnchor="middle"
                        dominantBaseline="middle"
                      >
                        <tspan
                          x={viewBox.cx}
                          y={viewBox.cy}
                          className="fill-foreground text-4xl font-bold text-black"
                        >
                          {currentVisitors.toLocaleString()}
                        </tspan>
                        <tspan
                          x={viewBox.cx}
                          y={(viewBox.cy || 0) + 24}
                          className="fill-muted-foreground text-black"
                        >
                          Patients
                        </tspan>
                      </text>
                    );
                  }
                }}
              />
            </PolarRadiusAxis>
          </RadialBarChart>
        </ChartContainer>
      </CardContent>
      <CardFooter className="flex-col gap-2 text-sm">
        <div className="leading-none text-muted-foreground text-center">
          Showing total number of patients in this medical institution.
        </div>
      </CardFooter>
    </Card>
  );
}
