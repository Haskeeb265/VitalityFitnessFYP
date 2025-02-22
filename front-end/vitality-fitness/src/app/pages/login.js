
import Image from "next/image";
import TextField from "@/components/TextField";
import Button from "@/components/Button";



export default function LoginPage() {
  return (
    <div className="login-container flex flex-col items-center justify-center h-screen">
        <div className="login-logo mb-[17px] ">
            <Image src="/img/login-logo.png" alt="Login Logo" width={120} height={120} />
        </div>
        <div className="login-heading mb-[31px]">
            <h1 className="text-[48px] text-[#DB4A2B] ">WELCOME TO VITALITY FITNESS</h1>
        </div>
        <div className="login-subheading mb-[17px]">
            <h2 className="text-[32px] sf-bold">LOGIN</h2>
        </div>
        <div className="login-subtext mb-[31px]">
            <h2 className="text-[16px]">Please enter your email and password</h2>
        </div>
        <div className="login-form">
        <form>
      <div className="email-field">
        <TextField label="Email:" id="email" placeholder="Enter your email" required />
      </div>
      <div className="password-field">
        <TextField label="Password:" id="password" type="password" placeholder="Enter your password" required />
      </div>
      <div className="forgot-password mb-[27px] flex justify-end underline decoration-solid">
          <a href="#" className="text-[12px] text-[#DB4A2B]">Forgot Password?</a>
      </div>
      <div className="login-btn">
      <Button type="submit">LOGIN</Button>
      </div> 
    </form>
        </div>
    </div>
);
}
