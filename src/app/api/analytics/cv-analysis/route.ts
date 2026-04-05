import { NextRequest, NextResponse } from 'next/server';
import connectDB from '@/lib/db/connection';
import CVAnalysis from '@/lib/db/models/CVAnalysis';
export async function GET(request: NextRequest) {
    try {
        await connectDB();
        // Total analyses
        const totalAnalyses = await CVAnalysis.countDocuments();
        // Average CV score
        const avgScoreResult = await CVAnalysis.aggregate([
            {
                $group: {
                    _id: null,
                    avgScore: { $avg: '$cvScore' },
                },
            },
        ]);
        const averageScore = avgScoreResult[0]?.avgScore || 0;
        // Monthly trend
        const monthlyTrend = await CVAnalysis.aggregate([
            {
                $group: {
                    _id: {
                        month: { $month: '$analysisDate' },
                        year: { $year: '$analysisDate' },
                    },
                    analyses: { $sum: 1 },
                    avgScore: { $avg: '$cvScore' },
                },
            },
            { $sort: { '_id.year': 1, '_id.month': 1 } },
            {
                $project: {
                    month: '$_id.month',
                    year: '$_id.year',
                    analyses: 1,
                    avgScore: { $round: ['$avgScore', 1] },
                    _id: 0,
                },
            },
        ]);
        return NextResponse.json({
            success: true,
            data: {
                totalAnalyses,
                averageScore: Math.round(averageScore * 10) / 10,
                monthlyTrend,
            },
        });
    } catch (error) {
        console.error('CV analysis analytics error:', error);
        return NextResponse.json(
            { error: 'Failed to fetch CV analytics' },
            { status: 500 }
        );
    }
}