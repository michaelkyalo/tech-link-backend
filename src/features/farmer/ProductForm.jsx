import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { getProduct } from "../farmer/productService";
import useCart from "./usecart";
import { formatCurrency } from "../../utils/helpers";

const ProductDetails = () => {
  const { id } = useParams();
  const [product, setProduct] = useState(null);
  const [wished, setWished] = useState(false);
  const [added, setAdded] = useState(false);
  const [qty, setQty] = useState(1);
  const { addToCart } = useCart();

  useEffect(() => {
    getProduct(id).then(setProduct).catch(console.error);
  }, [id]);

  const handleAddToCart = () => {
    addToCart({ ...product, quantity: qty });
    setAdded(true);
    setTimeout(() => setAdded(false), 2000);
  };

  if (!product) return (
    <div className="min-h-screen flex flex-col items-center justify-center gap-2 bg-[#f7f5f0]">
      <div className="w-8 h-8 border-2 border-green-600 border-t-transparent rounded-full animate-spin" />
      <span className="text-sm text-gray-400">Fetching product…</span>
    </div>
  );

  const initials = product.farmer_name
    ?.split(" ").map(n => n[0]).join("").slice(0, 2).toUpperCase() ?? "FM";

  return (
    <div className="min-h-screen bg-[#f7f5f0] flex items-center justify-center p-4 md:p-10">
      <div className="w-full max-w-4xl">

        {/* Breadcrumb */}
        <p className="text-xs text-gray-400 mb-4">
          Home &rsaquo; {product.category} &rsaquo;{" "}
          <span className="text-gray-700">{product.name}</span>
        </p>

        <div className="grid md:grid-cols-[1.1fr_1fr] gap-0 bg-white rounded-2xl overflow-hidden shadow-sm">

          {/* ── LEFT: Image ── */}
          <div className="relative bg-green-50 min-h-[420px]">
            <img
              src={product.image_url}
              alt={product.name}
              className="w-full h-full object-cover absolute inset-0"
            />

            {/* Overlay top bar */}
            <div className="absolute top-0 left-0 right-0 flex justify-between items-center p-4">
              <span className="bg-white text-green-700 text-[11px] font-semibold px-3 py-1 rounded-full uppercase tracking-wide">
                {product.category}
              </span>
              <button
                onClick={() => setWished(w => !w)}
                className="w-9 h-9 bg-white rounded-full flex items-center justify-center text-lg transition-transform hover:scale-110"
                aria-label="Wishlist"
              >
                {wished ? "❤️" : "🤍"}
              </button>
            </div>

            {/* Bottom stock ribbon */}
            <div className="absolute bottom-0 left-0 right-0 bg-black/40 backdrop-blur-sm px-4 py-3 flex justify-between items-center">
              <span className="text-white text-xs font-medium">
                🌿 Organically grown
              </span>
              <span className="text-white text-xs">
                <span className="inline-block w-2 h-2 rounded-full bg-green-400 mr-1" />
                {product.stock} in stock
              </span>
            </div>
          </div>

          {/* ── RIGHT: Details ── */}
          <div className="flex flex-col p-7 gap-5">

            {/* Title + Rating */}
            <div>
              <div className="flex items-center gap-2 mb-1">
                {"★★★★★".split("").map((s, i) => (
                  <span key={i} className="text-amber-400 text-sm">{s}</span>
                ))}
                <span className="text-xs text-gray-400 ml-1">(124 reviews)</span>
              </div>
              <h1 className="text-2xl font-extrabold text-gray-900 leading-tight">{product.name}</h1>
            </div>

            {/* Description */}
            <p className="text-sm text-gray-500 leading-relaxed border-l-4 border-green-200 pl-3">
              {product.description}
            </p>

            {/* Farmer card */}
            {product.farmer_name && (
              <div className="flex items-center gap-3 border border-gray-100 rounded-xl p-3 bg-gray-50">
                <div className="w-9 h-9 rounded-full bg-green-100 text-green-800 text-xs font-bold flex items-center justify-center shrink-0">
                  {initials}
                </div>
                <div>
                  <p className="text-sm font-semibold text-gray-800">{product.farmer_name}</p>
                  <p className="text-xs text-gray-400">📍 {product.location ?? "Local Farm"} · ✔ Verified Seller</p>
                </div>
              </div>
            )}

            {/* Meta pills */}
            <div className="flex flex-wrap gap-2">
              {[
                { label: "Weight", val: product.weight ?? "500g" },
                { label: "Delivery", val: product.delivery ?? "Same day" },
                { label: "Origin", val: product.origin ?? "Local" },
              ].map(({ label, val }) => (
                <div key={label} className="bg-gray-50 border border-gray-100 rounded-lg px-3 py-2 text-center min-w-[80px]">
                  <p className="text-[10px] uppercase tracking-widest text-gray-400">{label}</p>
                  <p className="text-xs font-semibold text-gray-700 mt-0.5">{val}</p>
                </div>
              ))}
            </div>

            {/* Price */}
            <div className="flex items-baseline gap-3">
              <span className="text-3xl font-black text-gray-900">{formatCurrency(product.price)}</span>
              <span className="text-xs text-gray-400">per unit</span>
            </div>

            {/* Qty selector + CTA */}
            <div className="flex items-center gap-3 mt-auto">
              <div className="flex items-center border border-gray-200 rounded-xl overflow-hidden">
                <button
                  onClick={() => setQty(q => Math.max(1, q - 1))}
                  className="px-3 py-2 text-lg text-gray-500 hover:bg-gray-100 transition-colors"
                >−</button>
                <span className="px-4 text-sm font-semibold text-gray-800">{qty}</span>
                <button
                  onClick={() => setQty(q => Math.min(product.stock, q + 1))}
                  className="px-3 py-2 text-lg text-gray-500 hover:bg-gray-100 transition-colors"
                >+</button>
              </div>

              <button
                onClick={handleAddToCart}
                className={`flex-1 py-3 rounded-xl text-sm font-bold tracking-wide transition-all active:scale-95 ${
                  added
                    ? "bg-green-100 text-green-700"
                    : "bg-green-700 hover:bg-green-800 text-white"
                }`}
              >
                {added ? "✓ Added to cart" : "Add to cart"}
              </button>
            </div>

          </div>
        </div>
      </div>
    </div>
  );
};

export default ProductDetails;