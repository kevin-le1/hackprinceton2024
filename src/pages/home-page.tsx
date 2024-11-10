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

import { useAuth0 } from "@auth0/auth0-react";

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
  const { loginWithRedirect } = useAuth0();

  const handleSignup = async () => {
    await loginWithRedirect({
      authorizationParams: {
        screen_hint: "signup",
      },
      appState: {
        returnTo: "/dashboard",
      },
    });
  };
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
                <Button
                  onClick={handleSignup}
                  className="bg-primary hover:bg-red2 text-white px-12 py-6 text-xl rounded-full transform transition-all duration-300 hover:scale-105 hover:shadow-xl"
                >
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
            className="py-24 px-8 bg-gradient-to-b from-secondary/10 to-transparent"
          >
            <div className="max-w-6xl mx-auto text-center">
              <h2 className="text-4xl md:text-5xl font-bold text-primary mb-8">
                Patient Care ♥ Secure Computing
              </h2>
              <p className="text-xl text-black/80 mb-16 max-w-3xl mx-auto">
                Using secure multipart computing, we help patients get the care
                they need while keeping their data private
              </p>
              <div className="grid md:grid-cols-2 gap-16 max-w-4xl mx-auto">
                <div className="space-y-6 bg-white/50 p-8 rounded-2xl shadow-lg">
                  <div className="w-16 h-16 bg-primary/10 rounded-full flex items-center justify-center mx-auto mb-4">
                    <svg
                      className="w-8 h-8 text-primary"
                      fill="currentColor"
                      viewBox="0 0 20 20"
                    >
                      <path d="M9 2a1 1 0 000 2h2a1 1 0 100-2H9z" />
                      <path
                        fillRule="evenodd"
                        d="M4 5a2 2 0 012-2 3 3 0 003 3h2a3 3 0 003-3 2 2 0 012 2v11a2 2 0 01-2 2H6a2 2 0 01-2-2V5zm3 4a1 1 0 000 2h.01a1 1 0 100-2H7zm3 0a1 1 0 000 2h3a1 1 0 100-2h-3zm-3 4a1 1 0 100 2h.01a1 1 0 100-2H7zm3 0a1 1 0 100 2h3a1 1 0 100-2h-3z"
                        clipRule="evenodd"
                      />
                    </svg>
                  </div>
                  <h3 className="text-2xl font-bold text-primary">
                    Risk Assessment
                  </h3>
                  <ul className="space-y-4 text-lg text-black/80">
                    <li>Calculate patient risk scores locally</li>
                    <li>Encrypt sensitive health data</li>
                    <li>Distribute encrypted data securely</li>
                    <li>Maintain complete patient privacy</li>
                  </ul>
                </div>
                <div className="space-y-6 bg-white/50 p-8 rounded-2xl shadow-lg">
                  <div className="w-16 h-16 bg-primary/10 rounded-full flex items-center justify-center mx-auto mb-4">
                    <svg
                      className="w-8 h-8 text-primary"
                      fill="currentColor"
                      viewBox="0 0 20 20"
                    >
                      <path d="M3 4a1 1 0 011-1h12a1 1 0 011 1v2a1 1 0 01-1 1H4a1 1 0 01-1-1V4zM3 10a1 1 0 011-1h6a1 1 0 011 1v6a1 1 0 01-1 1H4a1 1 0 01-1-1v-6zM14 9a1 1 0 00-1 1v6a1 1 0 001 1h2a1 1 0 001-1v-6a1 1 0 00-1-1h-2z" />
                    </svg>
                  </div>
                  <h3 className="text-2xl font-bold text-primary">
                    Global Queue
                  </h3>
                  <ul className="space-y-4 text-lg text-black/80">
                    <li>Create region-wide patient queues</li>
                    <li>Prioritize highest-risk patients</li>
                    <li>Process using secure computation</li>
                    <li>Optimize care across institutions</li>
                  </ul>
                </div>
              </div>
            </div>
          </motion.section>

          <motion.section
            initial={{ opacity: 0 }}
            whileInView={{ opacity: 1 }}
            transition={{ duration: 0.8 }}
            className="px-8"
          >
            <div className="max-w-6xl mx-auto">
              <h2 className="text-4xl md:text-5xl font-bold text-primary text-center">
                How It Works
              </h2>
            </div>
          </motion.section>

          <div className="w-full">
            <div className="space-y-8">
              <ImageTextSection
                imageSrc="src/images/stage1.svg"
                imageAlt="Connect Your Medicial Institution"
                title="Connect Your Medicial Institution"
                description="Participating medical institutions join a decentralized, peer-to-peer (P2P) network with other participating institutions in the same region; these entities work with the same medical specialists to provide necessary care to their patients."
              />

              <ImageTextSection
                imageSrc="src/images/stage2.svg"
                imageAlt="Enable New Insights"
                title="Enable New Insights"
                description="Medical institutions input patient data to determine risk scores. Data and computations are kept on-device to guarantee privacy."
                isImageLeft={false}
              />

              <ImageTextSection
                imageSrc="src/images/stage3.svg"
                imageAlt="Secure and Distributed Analytics"
                title="Secure and Distributed Analytics"
                description="We distribute Secure Multi-part Computation (SMC) across the P2P network to determine which patients need care the soonest. We know patient data is sensitive, so we ensure no other node can see patient data; instead data is encrypted locally and split into shares and distributed across the network."
              />

              <ImageTextSection
                imageSrc="src/images/stage4.svg"
                imageAlt="Creating a Global Queue with Only Local Information"
                title="Creating a Global Queue with Only Local Information"
                description="All participating medical institutions send their data (in the form of encrypted shares) to all other nodes in the network. All nodes then sort by patient risk score, in order to allocate the most immediate treatment with patients with the highest risk."
                isImageLeft={false}
              />
              <ImageTextSection
                imageSrc="src/images/stage5.svg"
                imageAlt="Helping Patients Get the Care They Need"
                title="Helping Patients Get the Care They Need"
                description="Medicial institutions see their patients with their positions in the global queue, without ever knowing any other patient data. This enables the patients with the most immediate needs to get the care they deserve."
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
              <Button
                onClick={handleSignup}
                className="bg-primary hover:bg-red2 text-white px-12 py-6 text-xl rounded-full transform transition hover:scale-105"
              >
                Sign Up Now
              </Button>
            </motion.section>
          </div>
        </main>

        <footer className="bg-secondary/40 mt-16 py-12">
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
