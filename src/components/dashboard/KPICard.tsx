import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { LucideIcon } from "lucide-react";

interface KPICardProps {
    title: string;
    value: string | number;
    icon: LucideIcon;
    trend?: { value: number; isPositive: boolean };
    description?: string;
}

export default function KPICard({ title, value, icon: Icon, trend, description }: KPICardProps) {
    return (
        <Card>
            <CardHeader className="flex flex-row items-center justify-between pb-2">
                <CardTitle className="text-sm font-medium text-muted-foreground">{title}</CardTitle>
                <Icon className="h-4 w-4 text-muted-foreground" />
            </CardHeader>
            <CardContent>
                <div className="text-2xl font-bold">{value}</div>
                {trend && (
                    <p className={`text-xs ${trend.isPositive ? "text-green-600" : "text-red-600"}`}>
                        {trend.isPositive ? "↑" : "↓"} {Math.abs(trend.value)}% from last month
                    </p>
                )}
                {description && (
                    <p className="text-xs text-muted-foreground mt-1">{description}</p>
                )}
            </CardContent>
        </Card>
    );
}
