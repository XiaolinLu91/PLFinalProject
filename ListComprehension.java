import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;
import java.util.stream.Collectors;


public class ListComprehension {
    ArrayList<Stock> sto = new ArrayList<>();
    ArrayList<Sector> sec = new ArrayList<>();

    public ListComprehension () throws IOException {
        //String path = System.getProperty("user.dir") + "/Documents/CS329E/Programming-Languages/Lu/PLFinalProject/";
        File file = new File("stocks.txt");
        BufferedReader br = new BufferedReader(new FileReader(file));
        String line;
        while ((line = br.readLine()) != null) {
            String a = line.substring(1, line.length() - 2);
            List<String> stockList = Arrays.asList(a.split(","));
            for (int i = 0; i < stockList.size(); i++) {
                stockList.set(i, stockList.get(i).trim());
            }
            stockList.get(0);
            Stock s = new Stock(stockList.get(0), stockList.get(1), stockList.get(2), Double.parseDouble(stockList.get(3)), Double.parseDouble(stockList.get(4)), Double.parseDouble(stockList.get(5)), stockList.get(6));
            sto.add(s);
        }

        br = new BufferedReader(new FileReader("sector.txt"));
        while ((line = br.readLine()) != null) {
            String a = line.substring(1, line.length() - 2);
            List<String> secList = Arrays.asList(a.split(","));
            Sector se = new Sector(secList.get(0), secList.get(1));
            sec.add(se);
        }
    }
    public void selectStocks() {
        // SELECT symble, name, sector FROM sto GROUP BY sector ORDER BY BV_share
            System.out.println("\nSELECT symble, name, sector FROM sto GROUP BY sector ORDER BY BV_share");
            sto.stream()
                    .collect(Collectors.groupingBy(Stock::getSector)) // This creates a map with the key of sector and value list of stocks in that sector
                    .entrySet() // this converts map into set that can be streamed
                    // e.g. {'Consumer Goods':[s1,s2,...],'Services':[s3,s4,....],...}
                    .stream()
                    .map(kv -> kv.getValue())
                    // this results in a streamed list of stocks
                    // l = [s1,s2,..]
                    .forEach((l) -> {
                        // l = [s1,s2,...] from a given sector
                        l.stream()
                                .sorted((s1, s2) -> Double.valueOf(s1.getBV_share())
                                        .compareTo(Double.valueOf(s2.getBV_share())))
                                .forEach(s -> {
                                    String toPrint = s.getSymble() + " " + s.getName() + " " + s.getSector();
                                    System.out.println(toPrint);
                                });
                    });
    }

        // SELECT symble, name FROM sto WHERE DE_ratio < # and current_ratio < #
    public void filterStocks(double DE_ratio, double current_ratio) {
        System.out.println("\nSELECT symble, name FROM sto WHERE DE_ratio < " +  DE_ratio + " and sec_name < " + current_ratio);
        sto.stream()
                .filter(s -> (s.getDE_ratio() < DE_ratio) && (s.getCurrent_ratio() < current_ratio ))
                .forEach(s -> {
                    String toPrint = s.getSymble() + " " + s.getName();
                    System.out.println(toPrint);
                });
    }

        // SELECT sector_id, avg(DE_ratio) FROM sto GROUP BY sector
    public void avgDEratio() {
        System.out.println("\nSELECT sec_id, avg(DEratio) FROM sto GROUP BY sector");
        sto.stream()
                .collect(Collectors.groupingBy(Stock::getSector)) // This creates a map with the key of sector and value list of stocks for that sector
                // {'Consumer Goods':[s1,s2,...],'Services':[s3,s4,....],...}
                .entrySet() // this converts map into set that can be streamed
                // {'Consumer Goods':[s1,s2,...],'Services':[s3,s4,....],...}
                .stream()
                .map(kv -> kv.getValue())
                // we have list of stockss for a given sector
                .forEach(stockList -> {
                    // stoList = [s1,s2,....] from a given sector
                    double avg = stockList
                            .stream()
                            .mapToDouble(s -> s.getDE_ratio())
                            // [s1,s2,...]
                            .average().getAsDouble();
                    String sector = stockList.get(0).getSector();
                    System.out.println(sector + " " + avg);
                });
    }

    public void allSector() {
        System.out.println("\nSELECT * FROM sec");
        sec.stream().forEach(s -> System.out.println(s));

    }

    public void orderStocks() {
        System.out.println("\nSELECT symble, name, current_ratio FROM sto ORDER BY current_ratio DESC");
        sto.stream()
                .sorted((s1, s2) -> Double.valueOf(s2.getCurrent_ratio()).compareTo(Double.valueOf(s1.getCurrent_ratio())))
                .forEach(s -> System.out.println(s.getSymble() + " " + s.getName() + " " + s.getCurrent_ratio()));
    }

}