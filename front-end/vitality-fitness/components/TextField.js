const TextField = ({ label, id, type = "text", placeholder, value, onChange }) => {
  return (
    <div className="flex items-center justify-between mb-[12px]">
      <label className="text-[12px] text-[#DB4A2B]" htmlFor={id}>
        {label}
      </label>
      <input
        className="text-[12px] pl-1 placeholder:text-[12px] ml-[26px] border border-[#DB4A2B] rounded w-[176px] h-[32px]"
        id={id}
        name={id}
        type={type}
        placeholder={placeholder}
        value={value} // <-- Ensures input reflects state
        onChange={onChange} // <-- Captures user input
      />
    </div>
  );
};

export default TextField;