import { useNavigate } from "react-router-dom";
import useCart from "./usecart";
import { formatCurrency } from "../../utils/helpers";

const ProductCard = ({ product }) => {
  const { addToCart } = useCart();
  const navigate = useNavigate();

  return (
    <div
      onClick={() => navigate(`/buyer/products/${product.id}`)}
      className="group bg-white rounded-2xl overflow-hidden border border-gray-100 shadow-sm hover:shadow-md transition-all duration-200 cursor-pointer"
    >
      {/* Image */}
      <div className="relative overflow-hidden h-48 bg-green-50">
        <img
          src={product.image_url}
          alt={product.name}
          className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300"
        />
        <span className="absolute top-3 left-3 bg-white text-green-700 text-[10px] font-semibold px-2 py-1 rounded-full uppercase tracking-wide border border-green-100">
          {product.category}
        </span>
      </div>

      {/* Body */}
      <div className="p-4 flex flex-col gap-2">
        <h2 className="text-sm font-bold text-gray-900 leading-snug line-clamp-1">
          {product.name}
        </h2>

        <p className="text-xs text-gray-400 line-clamp-2 leading-relaxed">
          {product.description}
        </p>

        <div className="flex items-center justify-between mt-2">
          <span className="text-lg font-black text-gray-900">
            {formatCurrency(product.price)}
          </span>

          <button
            onClick={(e) => {
              e.stopPropagation(); // prevents navigating when clicking Add to Cart
              addToCart(product);
            }}
            className="bg-green-700 hover:bg-green-800 active:scale-95 text-white text-xs font-semibold px-4 py-2 rounded-xl transition-all"
          >
            + Cart
          </button>
        </div>
      </div>
    </div>
  );
};

export default ProductCard;