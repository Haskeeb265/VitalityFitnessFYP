const Button = ({ children, type = "button", onClick }) => {
    return (
      <button
        className="mx-auto rounded-full bebas text-2xl flex items-center justify-center bg-[#DB4A2B] text-white w-[103px] h-[37px] hover:bg-[white] hover:text-[#DB4A2B] hover:border-[#DB4A2B] border border-[#DB4A2B] ease-in-out duration-300 cursor-pointer"
        type={type}
        onClick={onClick}
      >
        {children}
      </button>
    );
  };
  export default Button; 