import Image from "next/image";

export default function LoginPage() {
  
  return (
    <div className="login-container">


        <div className="login-logo ">
            <Image src="/img/login-logo.png" alt="Login Logo" width={120} height={120} />
        </div>
        
        <div className="login-heading">
            <h1 className="text-[48px] text-[#DB4A2B] ">WELCOME TO VITALITY FITNESS</h1>
        </div>

        <div className="login-subheading">
            <h2 className="text-[32px] sf-bold">LOGIN</h2>
        </div>

        <div className="login-subtext">
            <h2 className="text-[16px]">Please enter your email and password</h2>
        </div>


    </div>
  

);
}
