import { useEffect, useState } from "react";
import { getProducts, deleteProduct } from "./productService";
import { formatCurrency } from "../../utils/helpers";

const FarmerProducts = () => {
  const [products, setProducts] = useState([]);

  const fetchProducts = async () => {
    try {
      const data = await getProducts();
      setProducts(data);
    } catch (error) {
      console.error("Failed to fetch products:", error);
    }
  };

  useEffect(() => {
    fetchProducts();
  }, []);

const handleDelete = async (id) => {
    if (!confirm("Are you sure you want to delete this product?")) return;
    try {
        await deleteProduct(id);
        setProducts((prev) => prev.filter((p) => p.id !== id));
    } catch (error) {
        console.error("Failed to delete product:", error);
    }
};

return (
    <div className="min-h-screen bg-gray-100 p-6">
        {/* Header */}
        <div className="mb-8 flex items-center justify-between">
            <div>
                <h1 className="text-3xl font-bold text-green-700">My Products</h1>
                <p className="text-gray-600 mt-2">Manage your listed products</p>
            </div>
            <a
                href="/farmer/products/new"
                className="bg-green-600 text-white px-4 py-2 rounded-lg hover:bg-green-700 transition"
            >
                + Add Product
            </a>
        </div>

        {/* Products Table */}
        <div className="bg-white shadow rounded-lg overflow-x-auto">
            <table className="w-full border-collapse">
                <thead className="bg-green-600 text-white">
                    <tr>
                        <th className="text-left p-4">Product ID</th>
                        <th className="text-left p-4">Name</th>
                        <th className="text-left p-4">Category</th>
                        <th className="text-left p-4">Price</th>
                        <th className="text-left p-4">Stock</th>
                        <th className="text-left p-4">Status</th>
                        <th className="text-left p-4">Actions</th>
                    </tr>
                </thead>

                <tbody>
                    {products.length > 0 ? (
                        products.map((product) => (
                            <tr key={product.id} className="border-b hover:bg-gray-50">
                                <td className="p-4">#{product.id}</td>

                                <td className="p-4 flex items-center gap-3">
                                    {product.image_url && (
                                        <img
                                            src={product.image_url}
                                            alt={product.name}
                                            className="w-10 h-10 rounded object-cover"
                                        />
                                    )}
                                    {product.name}
                                </td>

                                <td className="p-4">{product.category}</td>

                                <td className="p-4">{formatCurrency(product.price)}</td>

                                <td className="p-4">{product.stock} units</td>

                                <td className="p-4">
                                    <span
                                        className={`px-3 py-1 rounded-full text-sm text-white ${product.status === "available"
                                                ? "bg-green-600"
                                                : product.status === "out_of_stock"
                                                    ? "bg-red-500"
                                                    : "bg-yellow-500"
                                            }`}
                                    >
                                        {product.status}
                                    </span>
                                </td>

                                <td className="p-4 flex gap-2">
                                    <a
                                        href={`/farmer/products/${product.id}/edit`}
                                        className="bg-blue-500 text-white px-3 py-1 rounded hover:bg-blue-600 text-sm"
                                    >
                                        Edit
                                    </a>
                                    <button
                                        onClick={() => handleDelete(product.id)}
                                        className="bg-red-500 text-white px-3 py-1 rounded hover:bg-red-600 text-sm"
                                    >
                                        Delete
                                    </button>
                                </td>
                            </tr>
                        ))
                    ) : (
                        <tr>
                            <td colSpan="7" className="text-center p-6 text-gray-500">
                                No products listed yet
                            </td>
                        </tr>
                    )}
                </tbody>
            </table>
        </div>
    </div>
);
};

export default FarmerProducts;

