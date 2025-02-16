"use client";

import { useState } from "react";
import Link from "next/link";
import Image from "next/image"; 

export default function Navbar() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <nav className="flex items-center justify-between p-4 bg-blue-500"> {/* Add flex properties */}
      <div className="flex items-center"> {/* Add flex properties */}
        <Link href="/">
          <Image src="/img/Logo.png" alt="Logo" width={200} height={200} /> 
        </Link>
        </div>

      <div className="navbar flex items-center">
        <ul className="nav-links flex space-x-4">
        <li><Link href="/" className="block">Home</Link></li>
        <li><Link href="/about" className="block">About</Link></li>
        <li><Link href="/services" className="block">Services</Link></li>
        <li><Link href="/contact" className="block">Contact</Link></li>
        </ul>
      </div>
    </nav>
  );
}