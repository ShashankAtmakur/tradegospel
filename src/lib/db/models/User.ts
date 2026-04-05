import mongoose, { Schema, models, model, Document } from "mongoose";

export interface IUser extends Document {
    name: string;
    email: string;
    password: string;
    role: "admin" | "user";
    country: string;
    careerStage: "Fresher" | "Graduate" | "Experienced";
    subscriptionType: "paid" | "free";
}

const UserSchema = new Schema<IUser>({
    name: { type: String, required: true },
    email: { type: String, required: true, unique: true },
    password: { type: String, required: true },
    role: { type: String, required: true, enum: ["admin", "user"], default: "user" },
    country: { type: String, required: true },
    careerStage: { type: String, enum: ["Fresher", "Graduate", "Experienced"], required: true },
    subscriptionType: { type: String, enum: ["paid", "free"], required: true, default: "free" }
}, { timestamps: true });

export default models.User || model<IUser>("User", UserSchema);
