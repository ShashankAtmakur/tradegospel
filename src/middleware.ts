import { NextRequest, NextResponse } from "next/server";
import { verifyToken } from "@/lib/auth/jwt";

export function middleware(request: NextRequest) {
    const token = request.cookies.get("token")?.value;
    const { pathname } = request.nextUrl;

    const publicRoutes = ["/login", "/register"];
    if (publicRoutes.includes(pathname)) return NextResponse.next();

    if (pathname.startsWith("/dashboard")) {
        if (!token) return NextResponse.redirect(new URL("/login", request.url));
        try {
            const payload = verifyToken(token);
            if (pathname.startsWith("/dashboard/admin") && payload.role !== "admin") {
                return NextResponse.redirect(new URL("/dashboard", request.url));
            }
            return NextResponse.next();
        } catch {
            return NextResponse.redirect(new URL("/login", request.url));
        }
    }
    return NextResponse.next();
}
export const config = { matcher: ["/((?!api|_next/static|_next/image|favicon.ico).*)"] };
