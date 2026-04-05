import { NextRequest, NextResponse } from "next/server";
import connectDB from "@/lib/db/connection";
import User from "@/lib/db/models/User";
import { hashPassword } from "@/lib/auth/password";
import { signToken } from "@/lib/auth/jwt";

export async function POST(request: NextRequest) {
    await connectDB();
    const { name, email, password, country, careerStage } = await request.json();
    if (!name || !email || !password) return NextResponse.json({ error: "Missing fields" }, { status: 400 });
    if (await User.findOne({ email })) return NextResponse.json({ error: "Already exists" }, { status: 409 });
    const hashedPassword = await hashPassword(password);
    const user = await User.create({ name, email, password: hashedPassword, country, careerStage, role: "user", subscriptionType: "free" });
    const token = signToken({ userId: user._id.toString(), email: user.email, role: user.role });
    const res = NextResponse.json({ success: true, token, user: { id: user._id, name: user.name, email: user.email, role: user.role } });
    res.cookies.set("token", token, { httpOnly: true });
    return res;
}
