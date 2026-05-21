
import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { getProduct } from "../farmer/productService";
import useCart from "./usecart";
import { formatCurrency } from "../../utils/helpers";
const ProductDetails = () => {
  const { id } = useParams();

  const [product, setProduct] = useState(null);

  const { addToCart } = useCart();

  useEffect(() => {
    fetchProduct();
  }, []);

  const fetchProduct = async () => {
    try {
      const data = await getProduct(id);
      setProduct(data);
    } catch (error) {
      console.error(error);
    }
  };

  if (!product) {
    return (
      <div className="p-6">
        Loading product...
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <div className="bg-white rounded-lg shadow p-6 grid md:grid-cols-2 gap-8">
        {/* Image */}
        <div>
          <img
            src={product.image_url}
            alt={product.name}
            className="w-full h-96 object-cover rounded"
          />
        </div>

        {/* Details */}
        <div>
          <h1 className="text-3xl font-bold mb-4">
            {product.name}
          </h1>

          <p className="text-gray-600 mb-4">
            {product.description}
          </p>

          <p className="text-lg mb-2">
            Category:
            <span className="font-semibold ml-2">
              {product.category}
            </span>
          </p>

          <p className="text-lg mb-4">
            Stock:
            <span className="font-semibold ml-2">
              {product.stock}
            </span>
          </p>

          <p className="text-3xl font-bold text-green-700 mb-6">
            {formatCurrency(product.price)}
          </p>

          <button
            onClick={() => addToCart(product)}
            className="bg-green-600 text-white px-6 py-3 rounded hover:bg-green-700"
          >
            Add To Cart
          </button>
        </div>
      </div>
    </div>
  );
};

export default ProductDetails;