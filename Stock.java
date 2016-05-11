public class Stock {
    private String id;
    private String symble;
    private String name;
    private double DE_ratio;
    private double current_ratio;
    private double BV_share;
    private String sector;



    public Stock(String id, String symble, String name, double DE_ratio, double current_ratio, double BV_share, String sector) {
        this.id = id;
        this.symble = symble;
        this.name = name;
        this.DE_ratio = DE_ratio;
        this.current_ratio = current_ratio;
        this.BV_share = BV_share;
        this.sector = sector;
    }

    public String getId() {
        return id;
    }

    public String getSymble() {
        return symble;
    }

    public String getName() {
        return name;
    }

    public double getDE_ratio() {
        return DE_ratio;
    }

    public double getCurrent_ratio() {
        return current_ratio;
    }

    public double getBV_share() {
        return BV_share;
    }

    public String getSector() {return sector; }


}