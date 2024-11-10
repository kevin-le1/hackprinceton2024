import Navbar from "../components/Navbar.tsx";
import { motion } from "framer-motion";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "../components/ui/card";
import { Button } from "../components/ui/button";

interface ImageTextSectionProps {
  imageSrc: string;
  imageAlt: string;
  title: string;
  description: string;
  isImageLeft?: boolean;
}

const ImageTextSection = ({
  imageSrc,
  imageAlt,
  title,
  description,
  isImageLeft = true,
}: ImageTextSectionProps) => {
  const containerVariants = {
    hidden: { opacity: 0, y: 50 },
    visible: {
      opacity: 1,
      y: 0,
      transition: {
        duration: 0.8,
        ease: "easeOut",
      },
    },
  };

  return (
    <motion.div
      initial="hidden"
      whileInView="visible"
      viewport={{ once: true, margin: "-100px" }}
      variants={containerVariants}
      className="py-24 px-8"
    >
      <div className="max-w-7xl mx-auto">
        <div
          className={`flex flex-col gap-8 ${
            isImageLeft ? "md:flex-row" : "md:flex-row-reverse"
          } items-center justify-between`}
        >
          <div className="w-full md:w-1/2">
            <div className="relative">
              <div className="absolute inset-0 bg-gradient-to-r from-white/40 to-transparent rounded-3xl blur-xl"></div>
              {imageSrc.endsWith(".svg") ? (
                <object
                  data={imageSrc}
                  type="image/svg+xml"
                  className="relative w-full h-[600px] rounded-3xl shadow-lg"
                  style={{
                    objectFit: "contain",
                    preserveAspectRatio: "xMidYMid meet",
                  }}
                >
                  <img
                    src={imageSrc}
                    alt={imageAlt}
                    className="relative w-full h-[600px] object-contain rounded-3xl shadow-lg"
                  />
                </object>
              ) : (
                <img
                  src={imageSrc}
                  alt={imageAlt}
                  className="relative w-full h-[600px] object-cover rounded-3xl shadow-lg"
                />
              )}
            </div>
          </div>
          <div className={`w-full md:w-5/12 space-y-8`}>
            <h2 className="text-4xl md:text-5xl font-bold text-[#E85A4F] leading-tight">
              {title}
            </h2>
            <p className="text-black text-xl md:text-2xl leading-relaxed">
              {description}
            </p>
          </div>
        </div>
      </div>
    </motion.div>
  );
};

export default function Home() {
  return (
    <div className="min-h-screen bg-background">
      <div
        className="relative"
        // style={{
        //   backgroundSize: "40px 40px",
        //   backgroundImage:
        //     "radial-gradient(circle, #000000 1px, rgba(0, 0, 0, 0) 1px)",
        // }}
      >
        <Navbar pageType="home" />

        <main>
          {/* Hero/Jumbotron Section */}
          <motion.section
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8 }}
            className="relative min-h-[90vh] flex items-center justify-center bg-gradient-to-b from-secondary/80 via-secondary/80 to-background"
          >
            <div className="container mx-auto px-4 text-center relative z-10">
              <motion.div
                initial={{ opacity: 0, y: 30 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.2, duration: 0.8 }}
                className="mb-8"
              >
                <span className="px-6 py-2 bg-primary/10 text-primary rounded-full text-sm font-semibold tracking-wide">
                  REVOLUTIONIZING HEALTHCARE
                </span>
              </motion.div>
              <motion.h1
                initial={{ opacity: 0, y: 30 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.4, duration: 0.8 }}
                className="text-6xl md:text-8xl font-extrabold text-primary mb-6 leading-tight"
              >
                Welcome to <br />
                <span className="bg-clip-text text-transparent bg-gradient-to-r from-primary to-red2">
                  HealthSync
                </span>
              </motion.h1>
              <motion.p
                initial={{ opacity: 0, y: 30 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.6, duration: 0.8 }}
                className="text-xl md:text-2xl text-black mb-12 max-w-3xl mx-auto font-light"
              >
                Your trusted partner in modern healthcare management and
                monitoring
              </motion.p>
              <motion.div
                initial={{ opacity: 0, y: 30 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.8, duration: 0.8 }}
              >
                <Button className="bg-primary hover:bg-red2 text-white px-12 py-6 text-xl rounded-full transform transition-all duration-300 hover:scale-105 hover:shadow-xl">
                  Get Started Today
                </Button>
              </motion.div>
            </div>
            <div className="absolute inset-0 bg-[url('/images/dots.svg')] opacity-5"></div>
            <div className="absolute bottom-0 left-0 right-0 h-32 bg-gradient-to-t from-background to-transparent"></div>
          </motion.section>

          <motion.section
            initial={{ opacity: 0 }}
            whileInView={{ opacity: 1 }}
            transition={{ duration: 0.8 }}
            className="py-24 px-8"
          >
            <div className="max-w-6xl mx-auto">
              <h2 className="text-4xl md:text-5xl font-bold text-primary text-center mb-16">
                How It Works
              </h2>
              <div className="grid md:grid-cols-2 gap-16">
                <div className="space-y-6">
                  <h3 className="text-3xl font-bold text-primary">
                    For Patients
                  </h3>
                  <ul className="space-y-4 text-xl text-black">
                    <li>Register and create your health profile</li>
                    <li>Connect with healthcare specialists</li>
                    <li>Monitor your health metrics in real-time</li>
                    <li>Receive personalized health insights</li>
                  </ul>
                </div>
                <div className="space-y-6">
                  <h3 className="text-3xl font-bold text-primary">
                    For Healthcare Providers
                  </h3>
                  <ul className="space-y-4 text-xl text-black">
                    <li>Access comprehensive patient health data</li>
                    <li>Monitor multiple patients efficiently</li>
                    <li>Receive alerts for critical changes</li>
                    <li>Collaborate with other specialists</li>
                  </ul>
                </div>
              </div>
            </div>
          </motion.section>

          <div className="w-full">
            <div className="space-y-8">
              <ImageTextSection
                imageSrc="src/images/stage1.svg"
                imageAlt="Real-time health monitoring"
                title="Real-time Health Monitoring"
                description="Our platform provides continuous health monitoring, allowing healthcare providers to track patient vitals and metrics in real-time. This immediate access to critical health data enables faster response times and better patient outcomes."
              />

              <ImageTextSection
                imageSrc="src/images/stage2.svg"
                imageAlt="Healthcare specialists"
                title="Connect with Specialists"
                description="Access a network of qualified healthcare specialists who can provide expert care and consultation. Our platform makes it easy to schedule appointments and receive personalized medical attention."
                isImageLeft={false}
              />

              <ImageTextSection
                imageSrc="src/images/stage3.svg"
                imageAlt="Health analytics dashboard"
                title="Smart Health Analytics"
                description="Leverage our advanced analytics tools to predict and prevent potential health issues. Our AI-powered system analyzes patterns in your health data to provide actionable insights and early warnings."
              />

              <ImageTextSection
                imageSrc="src/images/stage4.svg"
                imageAlt="Health analytics dashboard"
                title="Smart Health Analytics"
                description="Leverage our advanced analytics tools to predict and prevent potential health issues. Our AI-powered system analyzes patterns in your health data to provide actionable insights and early warnings."
                isImageLeft={false}
              />
              <ImageTextSection
                imageSrc="src/images/stage5.svg"
                imageAlt="Health analytics dashboard"
                title="Smart Health Analytics"
                description="Leverage our advanced analytics tools to predict and prevent potential health issues. Our AI-powered system analyzes patterns in your health data to provide actionable insights and early warnings."
              />
            </div>

            <motion.section
              initial={{ opacity: 0 }}
              whileInView={{ opacity: 1 }}
              transition={{ duration: 0.8 }}
              className="text-center max-w-4xl mx-auto py-24 px-8"
            >
              <h2 className="text-4xl md:text-5xl font-bold text-primary mb-8">
                Ready to Get Started?
              </h2>
              <p className="text-xl md:text-2xl text-black mb-12">
                Join thousands of patients and healthcare providers who trust
                HealthSync for better health outcomes.
              </p>
              <Button className="bg-primary hover:bg-red2 text-white px-12 py-6 text-xl rounded-full transform transition hover:scale-105">
                Sign Up Now
              </Button>
            </motion.section>
          </div>
        </main>

        <footer className="bg-secondary/80 mt-16 py-12">
          <div className="container mx-auto px-4">
            <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
              <div>
                <h3 className="text-xl font-bold text-primary mb-4">
                  HealthSync
                </h3>
                <p className="text-black">
                  Transforming healthcare through technology and innovation.
                </p>
              </div>
              <div>
                <h4 className="text-lg font-semibold text-primary mb-4">
                  Quick Links
                </h4>
                <ul className="space-y-2 text-black">
                  <li>About Us</li>
                </ul>
              </div>
              <div>
                <h4 className="text-lg font-semibold text-primary mb-4">
                  Legal
                </h4>
                <ul className="space-y-2 text-black">
                  <li>Privacy Policy</li>
                  <li>Terms of Service</li>
                </ul>
              </div>
              <div>
                <h4 className="text-lg font-semibold text-primary mb-4">
                  Connect
                </h4>
                <ul className="space-y-2 text-black">
                  <li>
                    <a
                      href="https://github.com/kevin-le1"
                      className="hover:text-red2"
                    >
                      @kevin-le1
                    </a>
                  </li>
                  <li>
                    <a
                      href="https://github.com/carterjc"
                      className="hover:text-red2"
                    >
                      @carterjc
                    </a>
                  </li>
                  <li>
                    <a
                      href="https://github.com/mz1231"
                      className="hover:text-red2"
                    >
                      @mz1231
                    </a>
                  </li>
                  <li>
                    <a
                      href="https://github.com/eugenechoi2004"
                      className="hover:text-red2"
                    >
                      @eugenechoi2004
                    </a>
                  </li>
                </ul>
              </div>
            </div>
            <div className="border-t border-black/20 mt-8 pt-8 text-center text-black">
              <p>
                &copy; {new Date().getFullYear()} HealthSync. All rights
                reserved.
              </p>
            </div>
          </div>
        </footer>
      </div>
    </div>
  );
}
