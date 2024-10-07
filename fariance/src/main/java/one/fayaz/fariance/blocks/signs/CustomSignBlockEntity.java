package one.fayaz.fariance.blocks.signs;

import net.minecraft.core.BlockPos;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.entity.BlockEntityType;
import net.minecraft.world.level.block.state.BlockState;

import net.minecraft.world.level.block.entity.SignBlockEntity;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.javafmlmod.FMLJavaModLoadingContext;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.ForgeRegistries;
import net.minecraftforge.registries.RegistryObject;
import one.fayaz.fariance.FarianceMod;
import one.fayaz.fariance.ItemRegistry;



@Mod.EventBusSubscriber(modid = FarianceMod.MODID, bus = Mod.EventBusSubscriber.Bus.MOD)
public class CustomSignBlockEntity extends SignBlockEntity {

    // The deferred register for block entity types
    public static final DeferredRegister<BlockEntityType<?>> BLOCK_ENTITY_TYPES = DeferredRegister.create(ForgeRegistries.BLOCK_ENTITY_TYPES, FarianceMod.MODID);
    public static RegistryObject<BlockEntityType<CustomSignBlockEntity>> CUSTOM_SIGN_BLOCK_ENTITY;

    // Constructor matching the parent class
    public CustomSignBlockEntity(BlockPos pos, BlockState state) {
        super(pos, state); // Calls the SignBlockEntity constructor
    }

    public static void registerBlockEntities() {
        CUSTOM_SIGN_BLOCK_ENTITY = BLOCK_ENTITY_TYPES.register(
                "custom_sign_block_entity",
                () -> BlockEntityType.Builder.of(CustomSignBlockEntity::new, // Correctly supply the constructor reference
                        ItemRegistry.GENERATED_BLOCKS.values().stream()
                                .filter(block -> block.get() instanceof CustomStandingSignBlock || block.get() instanceof CustomWallSignBlock)
                                .map(RegistryObject::get)
                                .toArray(Block[]::new) // Ensure the array type is Block[]
                ).build(null) // Build the BlockEntityType with a null constructor
        );

        BLOCK_ENTITY_TYPES.register(FMLJavaModLoadingContext.get().getModEventBus());
    }
}