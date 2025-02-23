import { NextResponse } from "next/server";
import connectToDatabase from "@/lib/mongodb";
import User from "@/models/User-login";
import jwt from "jsonwebtoken";

export async function POST(req) {
  try {
    await connectToDatabase();

    const { email, password } = await req.json();

    if (!email || !password) {
      return NextResponse.json({ message: "Email and password are required" }, { status: 400 });
    }

    // Find user in the database
    const user = await User.findOne({ email });

    if (!user || password !== user.password) {
      return NextResponse.json({ message: "Invalid email or password" }, { status: 400 });
    }

    // Generate JWT token
    console.log("JWT_SECRET:", process.env.JWT_SECRET);
    const token = jwt.sign({ userId: user._id }, process.env.JWT_SECRET, {
      expiresIn: "7d",
    });

    return NextResponse.json({ token, message: "Login successful" }, { status: 200 });
  } catch (error) {
    console.error("Login API Error:", error);
    return NextResponse.json({ message: "Internal Server Error", error: error.message }, { status: 500 });
  }
}



//This code will be used when we'll hash the password
// import connectToDatabase from "@/lib/mongodb"; 
// import User from "@/models/User";
// import jwt from "jsonwebtoken";

// export default async function handler(req, res) { 
//   if (req.method !== "POST") {
//     return res.status(405).json({ message: "Method Not Allowed" });
//   }

//   await connectToDatabase();

//   const { email, password } = req.body;

//   // Find user by email
//   const user = await User.findOne({ email });
//   if (!user) {
//     return res.status(400).json({ message: "Invalid email or password" });
//   }

//   // Compare passwords
//   const isMatch = await bcrypt.compare(password, user.password); 
//   if (!isMatch) {
//     return res.status(400).json({ message: "Invalid email or password" });
//   }

//   // Generate JWT token
//   const token = jwt.sign({ userId: user._id }, process.env.JWT_SECRET, {
//     expiresIn: "7d",
//   });

//   res.status(200).json({ token, message: "Login successful" });
// } 
