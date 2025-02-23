const Button = ({ children, type = "button", onClick }) => {
    return (
      <button
        className="px-4 mx-auto rounded-[5px] bebas text-lg flex items-center justify-between bg-[#ffffff] text-black w-[190px] h-10 hover:bg-[white] hover:text-[#DB4A2B] hover:border-[#DB4A2B] border border-[#000000] ease-in-out duration-300 cursor-pointer"
        type={type}
        onClick={onClick}
      >
        {children}
      </button>
    );
  };
  export default Button; 