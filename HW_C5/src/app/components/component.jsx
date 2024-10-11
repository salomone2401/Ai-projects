import Image from 'next/image'
import { ChevronDown, MonitorSmartphone, BookOpen, Users, ShieldCheck } from 'lucide-react'

export default function Component() {
  return (
    <div className="min-h-screen flex flex-col font-['__SatoshiBold_aaba03,__SatoshiBold_Fallback_aaba03']">
      <header className="container mx-auto px-4 py-4 flex items-center">
        <Image src="https://www.soyhenry.com/_next/static/media/HenryLogo.bb57fd6f.svg" 
        alt="Bootcamp Logo" width={120} height={40} priority
        />
        <nav className="hidden md:flex items-center space-x-6 ml-8">
          <div className="flex items-center font-['__SatoshiBold_aaba03,__SatoshiBold_Fallback_aaba03'] font-bold">
            Para estudiantes <ChevronDown className="ml-1 h-4 w-4" />
          </div>
          <div className="flex items-center font-['__SatoshiBold_aaba03,__SatoshiBold_Fallback_aaba03'] font-bold">
            Para empresas <ChevronDown className="ml-1 h-4 w-4" />
          </div>
        </nav>
        <div className="ml-auto flex items-center space-x-4">
          <button className="text-gray-600 hover:text-gray-800">Ingresar</button>
          <button className="bg-yellow-400 text-black px-4 py-2 rounded-md hover:bg-yellow-500">
            Aplicar
          </button>
        </div>
        <button className="md:hidden ml-4">Menu</button>
      </header>

      <main className="flex-grow container mx-auto px-4 py-8 md:py-16 flex flex-col md:flex-row items-center">
        <div className="md:w-1/2 md:pr-8">
          <h1 className="text-4xl md:text-5xl font-bold leading-tight mb-4">
            Comienza o acelera tu carrera en tecnología
          </h1>
          <p className="text-xl mb-6">
            Estudia Desarrollo Full Stack, Data Science o Data Analytics.
          </p>
          <ul className="space-y-4 mb-8">
            <li className="flex items-center">
              <MonitorSmartphone className="h-6 w-6 text-purple-600 mr-2" />
              <span>Online, en vivo y flexible</span>
            </li>
            <li className="flex items-center">
              <BookOpen className="h-6 w-6 text-purple-600 mr-2" />
              <span>Basado en proyectos</span>
            </li>
            <li className="flex items-center">
              <Users className="h-6 w-6 text-purple-600 mr-2" />
              <span>Basado en cohortes</span>
            </li>
            <li className="flex items-center">
              <ShieldCheck className="h-6 w-6 text-purple-600 mr-2" />
              <span>Garantía de Empleo</span>
            </li>
          </ul>
          <button className="bg-yellow-400 text-black px-6 py-3 rounded-md text-lg font-semibold hover:bg-yellow-500">
            Aplicar
          </button>
        </div>
        <div className="md:w-1/2 mt-8 md:mt-0">
          <Image
            src="/image.png"
            alt="Mujer aprende desarrollo web full stack en Henry"
            width={640}
            height={713}
            className="page_hero-image__l_z7X rounded-[2.5rem]"
            priority
          />
        </div>
      </main>

      <footer className="container mx-auto px-4 py-8 text-center">
        <p className="text-xl font-semibold">
          Bootcamp <span className="text-purple-600">#1</span> de Latam
        </p>
      </footer>
    </div>
    )
}