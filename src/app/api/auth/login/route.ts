import { NextRequest, NextResponse } from "next/server";
import connectDB from "@/lib/db/connection";
import User from "@/lib/db/models/User";
import { comparePassword } from "@/lib/auth/password";
import { signToken } from "@/lib/auth/jwt";

export async function POST(request: NextRequest) {
    await connectDB();
    const { email, password } = await request.json();
    const user = await User.findOne({ email });
    if (!user || !(await comparePassword(password, user.password))) {
        return NextResponse.json({ error: "Invalid credentials" }, { status: 401 });
    }
    const token = signToken({ userId: user._id.toString(), email: user.email, role: user.role });
    const res = NextResponse.json({ success: true, token, user: { id: user._id, name: user.name, email: user.email, role: user.role } });
    res.cookies.set("token", token, { httpOnly: true });
    return res;
}
