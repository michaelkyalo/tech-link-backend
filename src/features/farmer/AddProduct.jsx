import { useState } from "react";
import { createProduct } from "./productService";

const AddProduct = () => {
  const [form, setForm] = useState({
    name: "",
    description: "",
    price: "",
    image_url: "",
  });

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    await createProduct(form);

    alert("Product added successfully");

    setForm({
      name: "",
      description: "",
      price: "",
      image_url: "",
    });
  };

  return (
    <div className="max-w-lg mx-auto p-6">
      <h1 className="text-2xl font-bold mb-4">
        Add Product
      </h1>

      <form
        onSubmit={handleSubmit}
        className="space-y-4"
      >
        <input
          name="name"
          placeholder="Product Name"
          value={form.name}
          onChange={handleChange}
          className="border p-2 w-full"
        />

        <textarea
          name="description"
          placeholder="Description"
          value={form.description}
          onChange={handleChange}
          className="border p-2 w-full"
        />

        <input
          name="price"
          placeholder="Price"
          value={form.price}
          onChange={handleChange}
          className="border p-2 w-full"
        />

        <input
          name="image_url"
          placeholder="Image URL"
          value={form.image_url}
          onChange={handleChange}
          className="border p-2 w-full"
        />

        <button className="bg-green-600 text-white px-4 py-2">
          Add Product
        </button>
      </form>
    </div>
  );
};

export default AddProduct;