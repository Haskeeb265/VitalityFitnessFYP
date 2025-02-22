import Image from "next/image";

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
      <div className="flex items-center justify-between mb-[12px]">
        <label className="text-[12px] text-[#DB4A2B]" htmlFor="email">Email:</label>
        <input className="placeholder:text-[12px] ml-[26px] border border-[#DB4A2B] rounded w-[176px] h-[32px]" id="email" name="email" placeholder="  Enter your email" />
      </div>
      <div className="flex items-center justify-between mb-[15px] ">
        <label className="text-[12px] text-[#DB4A2B]" htmlFor="password">Password: </label>
        <input className="placeholder:text-[12px] ml-[26px] border border-[#DB4A2B] rounded w-[176px] h-[32px]" placeholder=" Enter your password"  id="password" name="password" type="password" />
      </div>
      <div className="forgot-password mb-[27px] flex justify-end underline decoration-solid">
          <a href="#" className="text-[12px] text-[#DB4A2B]">Forgot Password?</a>
      </div>
      <div className="login-btn mx-auto rounded-full bebas text-[20px] flex items-center justify-center bg-[#DB4A2B] text-white w-[103px] h-[37px] hover:bg-[white] hover:text-[#DB4A2B] hover:border-[#DB4A2B] border border-[#DB4A2B] hover: ease-in-out duration-300 hover:cursor-pointer">
      <button className="hover:cursor-pointer" type="submit">LOGIN</button>
      </div> 
    </form>
        </div>
    </div>
  

);
}
