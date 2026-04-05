import mongoose, { Schema, models, model, Document } from "mongoose";

export interface IFeedback extends Document {
    userId: mongoose.Types.ObjectId;
    rating: number;
    category: "UI/UX" | "Accuracy" | "Speed" | "Support";
    comment?: string;
    createdAt: Date;
}

const FeedbackSchema = new Schema<IFeedback>({
    userId: { type: Schema.Types.ObjectId, ref: "User", required: true },
    rating: { type: Number, required: true, min: 1, max: 5 },
    category: { type: String, enum: ["UI/UX", "Accuracy", "Speed", "Support"], required: true },
    comment: { type: String },
    createdAt: { type: Date, default: Date.now }
});

export default models.Feedback || model<IFeedback>("Feedback", FeedbackSchema);
