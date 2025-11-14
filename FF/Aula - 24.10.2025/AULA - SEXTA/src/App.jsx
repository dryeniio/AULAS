import { useState, useEffect } from "react";
import Button from "./components/Button";

function App() {
  const [idade, setIdade] = useState(0);
  const [nome, setNome] = useState('');
  const [contador, setContador] = useState(0);
  useEffect(() => {
    setTimeout(() => {
      setContador(contador) -> contador + 1);
    }, 1000);
  }");