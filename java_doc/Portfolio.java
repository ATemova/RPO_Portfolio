/**
 * Predstavitveni razred za osebni portfelj.
 * Vsebuje osnovne podatke (ime, e-pošta, GitHub) in metode za izpis predstavitve.
 *
 * <p>Namen: prikaz uporabe Javadoc v okviru naloge RPO.</p>
 *
 * @author Anastasija Temova
 * @version 1.0
 */
public class Portfolio {

    private String authorName;
    private String email;
    private String githubLink;

    /**
     * Ustvari nov portfelj.
     *
     * @param authorName ime avtorja
     * @param email e-pošta avtorja
     * @param githubLink povezava do GitHub profila
     */
    public Portfolio(String authorName, String email, String githubLink) {
        this.authorName = authorName;
        this.email = email;
        this.githubLink = githubLink;
    }

    /**
     * Nastavi e-pošto (preveri osnovno veljavnost).
     *
     * @param email nova e-pošta
     * @throws IllegalArgumentException če je e-pošta prazna ali brez znaka '@'
     */
    public void setEmail(String email) {
        if (email == null || email.isBlank() || !email.contains("@")) {
            throw new IllegalArgumentException("Neveljaven e-poštni naslov.");
        }
        this.email = email;
    }

    /**
     * Vrne kratko predstavitev avtorja.
     *
     * @return niz s kratko predstavitvijo
     */
    public String getIntroduction() {
        return "Hello, I am " + authorName + " — computer science student. "
                + "You can write to me " + email + " or see my work here: " + githubLink + ".";
    }

    /**
     * Izpiše predstavitev v konzolo.
     */
    public void printIntroduction() {
        System.out.println(getIntroduction());
    }

    /**
     * Vstopna točka programa (demo).
     *
     * @param args argumenti ukazne vrstice (neuporabljeno)
     */
    public static void main(String[] args) {
        Portfolio p = new Portfolio(
                "Anastasija Temova",
                "temanastasa@gmail.com",
                "https://github.com/ATemova"
        );
        p.printIntroduction();
    }
}