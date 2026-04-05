'use client';

import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import {
    LineChart,
    Line,
    XAxis,
    YAxis,
    CartesianGrid,
    Tooltip,
    Legend,
    ResponsiveContainer
} from 'recharts';

// Define the data type for chart entries
export interface TrendData {
    month: string;       // 'Jan', 'Feb', ...
    analyses: number;    // number of CV analyses that month
    avgScore: number;    // average CV score for that month
}

export interface CVTrendChartProps {
    data: TrendData[];
}

export default function CVTrendChart({ data }: CVTrendChartProps) {
    return (
        <Card>
            <CardHeader>
                <CardTitle>CV Analysis Trend</CardTitle>
            </CardHeader>
            <CardContent>
                <ResponsiveContainer width="100%" height={300}>
                    <LineChart data={data}>
                        <CartesianGrid strokeDasharray="3 3" />
                        <XAxis dataKey="month" />
                        <YAxis yAxisId="left" label={{ value: "Analyses", angle: -90, position: 'insideLeft' }} />
                        <YAxis
                            yAxisId="right"
                            orientation="right"
                            label={{ value: "Avg Score", angle: 90, position: 'insideRight' }}
                        />
                        <Tooltip />
                        <Legend />
                        <Line
                            yAxisId="left"
                            type="monotone"
                            dataKey="analyses"
                            name="Analyses"
                            stroke="#3b82f6"
                            strokeWidth={2}
                            activeDot={{ r: 7 }}
                        />
                        <Line
                            yAxisId="right"
                            type="monotone"
                            dataKey="avgScore"
                            name="Avg Score"
                            stroke="#10b981"
                            strokeWidth={2}
                            dot={{ r: 5 }}
                        />
                    </LineChart>
                </ResponsiveContainer>
            </CardContent>
        </Card>
    );
}
