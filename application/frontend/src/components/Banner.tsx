export default function Banner() {
  return (
    <div className="relative w-full h-56 overflow-hidden shadow-md rounded-md">
      <div
        className="absolute inset-0 bg-[url(/src/assets/wheat_tech.jpg)] bg-cover bg-[center_30%] bg-no-repeat"
      />
      <div className="relative z-10 flex items-end justify-start h-full">
        <h1 className="text-white text-xl md:text-2xl lg:text-3xl font-bold drop-shadow-lg text-center m-8">
          DeepWheat: AI-Powered Wheat Health Monitoring
        </h1>
      </div>
    </div>

  );
}
