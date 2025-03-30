import { createContext, useContext, useState, ReactNode } from 'react';

type Page = 'home' | 'dashboard' | 'users' | 'analytics';

interface NavigationContextType {
  currentPage: Page;
  setCurrentPage: (page: Page) => void;
}

const NavigationContext = createContext<NavigationContextType>({
  currentPage: 'dashboard',
  setCurrentPage: () => {}
});

export const NavigationProvider = ({ children }: { children: ReactNode }) => {
  const [currentPage, setCurrentPage] = useState<Page>('dashboard');
  
  return (
    <NavigationContext.Provider value={{ currentPage, setCurrentPage }}>
      {children}
    </NavigationContext.Provider>
  );
};

export const useNavigation = () => useContext(NavigationContext);