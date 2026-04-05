import mongoose, { Schema, models, model, Document } from "mongoose";

export interface ICVAnalysis extends Document {
    userId: mongoose.Types.ObjectId;
    cvScore: number;
    analysisDate: Date;
    skills: string[];
    experience: number;
    education: string;
    sections?: Record<string, number>;
}
const CVAnalysisSchema = new Schema<ICVAnalysis>({
    userId: { type: Schema.Types.ObjectId, ref: "User", required: true },
    cvScore: { type: Number, required: true, min: 0, max: 100 },
    analysisDate: { type: Date, default: Date.now },
    skills: [{ type: String }],
    experience: { type: Number },
    education: { type: String },
    sections: { type: Object }
});

export default models.CVAnalysis || model<ICVAnalysis>("CVAnalysis", CVAnalysisSchema);
