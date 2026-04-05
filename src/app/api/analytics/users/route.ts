import { NextRequest, NextResponse } from "next/server";
import connectDB from "@/lib/db/connection";
import User from "@/lib/db/models/User";

export async function GET(request: NextRequest) {
    await connectDB();
    const totalUsers = await User.countDocuments();
    const paidUsers = await User.countDocuments({ subscriptionType: "paid" });
    const freeUsers = await User.countDocuments({ subscriptionType: "free" });
    const usersByCountry = await User.aggregate([{ $group: { _id: "$country", count: { $sum: 1 } } }, { $project: { country: "$_id", count: 1, _id: 0 } }, { $sort: { count: -1 } }]);
    const usersByCareerStage = await User.aggregate([{ $group: { _id: "$careerStage", count: { $sum: 1 } } }, { $project: { stage: "$_id", count: 1, _id: 0 } }]);
    return NextResponse.json({ totalUsers, paidUsers, freeUsers, usersByCountry, usersByCareerStage });
}
