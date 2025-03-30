import React, { createContext, useState, useContext } from 'react';

type NavigationContextType = {
  currentPage: string;
  setCurrentPage: (page: string) => void;
};

const NavigationContext = createContext<NavigationContextType>({
  currentPage: 'home',
  setCurrentPage: () => {},
});

export const NavigationProvider: React.FC<{children: React.ReactNode}> = ({ children }) => {
  const [currentPage, setCurrentPage] = useState('home');

  return (
    <NavigationContext.Provider value={{ currentPage, setCurrentPage }}>
      {children}
    </NavigationContext.Provider>
  );
};

export const useNavigation = () => useContext(NavigationContext);